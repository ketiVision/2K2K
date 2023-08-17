import numpy as np
import os
import cv2
import trimesh
import collections
import torch
import math
from lib.renderer.camera import Camera
from neural_renderer import renderer as nr

def get_normal(x, normalize=True, cut_off=0.2):
    def gradient_x(img):
        img = torch.nn.functional.pad (img, (0, 0, 1, 0), mode="replicate")  # pad a column to the end
        gx = img[:, :, :-1, :] - img[:, :, 1:, :]
        return gx

    def gradient_y(img):
        img = torch.nn.functional.pad (img, (0, 1, 0, 0), mode="replicate")  # pad a row on the bottom
        gy = img[:, :, :, :-1] - img[:, :, :, 1:]
        return gy

    def normal_from_grad(grad_x, grad_y, depth, pred_res=512):

        if pred_res == 512:
            scale = 4.0
        elif pred_res == 1024:
            scale = 8.0
        elif pred_res == 2160:
            scale = 16.0

        grad_z = torch.ones_like(grad_x) / scale  # scaling factor (to magnify the normal)
        n = torch.sqrt(torch.pow(grad_x, 2) + torch.pow(grad_y, 2) + torch.pow(grad_z, 2))
        normal = torch.cat((grad_y / n, grad_x / n, grad_z / n), dim=1)

        # remove normals along the object discontinuities and outside the object.
        # normal[depth.repeat(1, 3, 1, 1) < cut_off] = 0
        return normal

    if x is None:
        return None

    if len(x.shape) == 3:
        x = x.unsqueeze(1)

    x = x.float()
    # temporary code. 220.0 = distance from the object to the camera.
    if torch.max(x) < 1.0:
        x = (x - 0.5) * 128.0 + 220.0
    grad_x = gradient_x(x)
    grad_y = gradient_y(x)

    if x.shape[1] == 1:
        return normal_from_grad(grad_x, grad_y, x)
    else:
        normal = [normal_from_grad
                  (grad_x[:, k, :, :].unsqueeze(1), grad_y[:, k, :, :].unsqueeze(1), x[:, k, :, :].unsqueeze(1)) for k in range(x.shape[1])]
        return torch.cat(normal, dim=1)
def make_rotate(rx, ry, rz):
    sinX = np.sin(rx)
    sinY = np.sin(ry)
    sinZ = np.sin(rz)

    cosX = np.cos(rx)
    cosY = np.cos(ry)
    cosZ = np.cos(rz)

    Rx = np.zeros((3,3))
    Rx[0, 0] = 1.0
    Rx[1, 1] = cosX
    Rx[1, 2] = -sinX
    Rx[2, 1] = sinX
    Rx[2, 2] = cosX

    Ry = np.zeros((3,3))
    Ry[0, 0] = cosY
    Ry[0, 2] = sinY
    Ry[1, 1] = 1.0
    Ry[2, 0] = -sinY
    Ry[2, 2] = cosY

    Rz = np.zeros((3,3))
    Rz[0, 0] = cosZ
    Rz[0, 1] = -sinZ
    Rz[1, 0] = sinZ
    Rz[1, 1] = cosZ
    Rz[2, 2] = 1.0

    R = np.matmul(np.matmul(Rz,Ry),Rx)
    return R

def load_obj_mesh(mesh_file, texture, with_normal=False, with_texture=False):
    vertex_data = []
    norm_data = []
    uv_data = []
    dict = collections.defaultdict(int)

    face_data = []
    face_norm_data = []
    face_uv_data = []

    if isinstance(mesh_file, str):
        f = open(mesh_file, "r")
    else:
        f = mesh_file

    for line in f:
        if isinstance(line, bytes):
            line = line.decode("utf-8")
        if line.startswith('#'):
            continue
        values = line.split()
        if not values:
            continue
        if values[0] == 'v':
            v = list(map(float, values[1:4]))
            vertex_data.append(v)
        elif values[0] == 'vn':
            vn = list(map(float, values[1:4]))
            norm_data.append(vn)
        elif values[0] == 'vt':
            vt = list(map(float, values[1:3]))
            uv_data.append(vt)
        elif values[0] == 'f':
            # quad mesh
            if len(values) > 4:
                f = list(map(lambda x: int(x.split('/')[0]), values[1:4]))
                face_data.append(f)
                f = list(map(lambda x: int(x.split('/')[0]), [values[3], values[4], values[1]]))
                face_data.append(f)
            # tri mesh
            else:
                f = list(map(lambda x: int(x.split('/')[0]), values[1:4]))
                face_data.append(f)

            # deal with texture
            if len(values[1].split('/')) >= 2:
                # quad mesh
                if len(values) > 4:
                    f = list(map(lambda x: int(x.split('/')[1]), values[1:4]))
                    face_uv_data.append(f)
                    f = list(map(lambda x: int(x.split('/')[1]), [values[3], values[4], values[1]]))
                    face_uv_data.append(f)
                # tri mesh
                elif len(values[1].split('/')[1]) != 0:
                    f_c = list(map(lambda x: int(x.split('/')[1]), values[1:4]))
                    face_uv_data.append(f_c)
                    f = list(map(lambda x: int(x.split('/')[0]), values[1:4]))
                    dict[f[0] - 1] = f_c[0] - 1
                    dict[f[1] - 1] = f_c[1] - 1
                    dict[f[2] - 1] = f_c[2] - 1
                else:
                    face_uv_data.append([1, 1, 1])

            # deal with normal
            if len(values[1].split('/')) == 3:
                # quad mesh
                if len(values) > 4:
                    f = list(map(lambda x: int(x.split('/')[2]), values[1:4]))
                    face_norm_data.append(f)
                    f = list(map(lambda x: int(x.split('/')[2]), [values[3], values[4], values[1]]))
                    face_norm_data.append(f)
                # tri mesh
                elif len(values[1].split('/')[2]) != 0:
                    f = list(map(lambda x: int(x.split('/')[2]), values[1:4]))
                    face_norm_data.append(f)

    vertex_colors = []
    for k in range(len(vertex_data)):
        if k in dict:
            vertex_colors.append(uv_data[dict[k]])
        else:
            vertex_colors.append([0.0, 0.0])

    w, h = texture.shape[0], texture.shape[1]

    vertices = np.array(vertex_data)
    visuals = np.array(vertex_colors)
    faces = np.array(face_data) - 1

    vertex_colors = visuals
    vertex_colors = [[int(item[0] * w), int(item[1] * h)] for item in vertex_colors]
    vertex_colors = [texture[item[1], item[0], :] for item in vertex_colors]
    visuals = np.array(vertex_colors)
    mesh = trimesh.Trimesh(vertices=vertices, faces=faces, vertex_colors=visuals, process=True)

    return mesh

if __name__ == '__main__':
    img_size = 512
    cam = Camera(width=img_size,
                 height=img_size,
                 projection='perspective')
    renderer = nr.Renderer(image_size=img_size,
                           orig_size=img_size,
                           anti_aliasing=True,
                           camera_direction=[0, 0, -1],
                           camera_mode='projection',
                           viewing_angle=0,
                           light_color_directional=[1, 1, 1],
                           light_intensity_directional=0.3,
                           light_intensity_ambient=0.7,
                           light_direction=[0, -0.7, -1],
                           near=1, far=600)
    cam.z_near = 1
    cam.z_far = 600
    cam.center = np.array([0, 0, 300.0])
    device = torch.device("cuda:0")

    path = '/data/2k2k/train/50K'
    save_path = path + '/render'
    os.makedirs(save_path, exist_ok=True)
    datalist = sorted(os.listdir(path))

    R_np, K_np, t_np, _, _ = cam.get_gl_matrix()
    K = torch.tensor(K_np[None, :, :]).float().to(device)
    t = torch.tensor(t_np[None, :]).float().to(device)
    idx = 1
    for dataname in sorted(datalist):
        data_path = os.path.join(path, dataname, '%s.ply' % dataname)
        os.makedirs(save_path + '/%s' % dataname, exist_ok=True)
        data = trimesh.load_mesh(data_path, process=True)
        print(str(idx)+'......'+'%s.ply' % dataname)
        idx += 1
        vertices = data.vertices
        vmin = vertices.min(0)
        vmax = vertices.max(0)
        up_axis = 1 if (vmax - vmin).argmax() == 1 else 2

        center = np.median(vertices, 0)
        center[up_axis] = 0.5 * (vmax[up_axis] + vmin[up_axis])
        scale = 180 / (vmax[up_axis] - vmin[up_axis])
        vertices -= center
        vertices *= scale
        data.vertices = vertices

        verts = torch.Tensor(data.vertices).unsqueeze(0).to(device)
        faces = torch.tensor(data.faces[None, :, :].copy()).float().to(device)
        textr_face = torch.tensor(data.visual.face_colors[None, :, -2:-5:-1].copy()).float().to(device) / 255.0
        textr_face = textr_face.unsqueeze(2).unsqueeze(2).unsqueeze(2)
        pitch = [0]
        for k in range(len(pitch)):
            pit = pitch[k]
            for vid in range(0, 360, 3):
                R_delta = np.matmul(make_rotate(math.radians(pit), 0, 0), make_rotate(0, math.radians(vid), 0))
                R = np.matmul(R_np, R_delta)
                R = torch.tensor(R[None, :, :]).float().to(device)
                images_out, depth_out, silhouette_out = renderer(verts, faces, textr_face,    K=K, R=R, t=t)
                image = images_out.squeeze().permute(2, 1, 0).detach().cpu().numpy()
                image = np.flip(np.rot90(image, -1), 1)
                image_out = (image / np.max(image) * 255.0).astype(np.uint8)
                cv2.imwrite(save_path+'/%s/%d_%d.jpg' % (dataname, pit, vid), image_out)
