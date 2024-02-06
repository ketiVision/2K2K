# 2K2K Dataset
### High-fidelity 3D Human Digitization from Single 2K Resolution Images
[Sang-Hun Han](https://sanghunhan92.github.io/conference/2K2K/), [Min-Gyu Park](https://scholar.google.co.uk/citations?user=VUj1ZWoAAAAJ&hl=en), [Ju Hong Yoon](https://scholar.google.com/citations?user=Y4mReV4AAAAJ&hl=en), Ju-Mi Kang, Young-Jae Park and [Hae-Gon Jeon](https://sites.google.com/site/hgjeoncv/).  CVPR 2023

[[Project Page]](https://sanghunhan92.github.io/conference/2K2K/)

<br/>
<p align="center">
  <img src="./2K2K - 1.png"/>
</p>



### Agreement
1. The 2K2K dataset (the "Dataset") is available for **non-commercial** research purposes only. Any other use, in particular any use for commercial purposes, is prohibited. This includes, without limitation, incorporation in a commercial product, use in a commercial service, as training data for a commercial product, for commercial ergonomic analysis (e.g. product design, architectural design, etc.), or production of other artifacts for commercial purposes including, for example, web services, movies, television programs, mobile applications, or video games. The Dataset may not be used for pornographic purposes or to generate pornographic material whether commercial or not. The Dataset may not be reproduced, modified and/or made available in any form to any third party without [IOYS](http://ioys.co.kr/)’s prior written permission.

2. You agree **not to** reproduce, modify, duplicate, copy, sell, trade, resell, or exploit any portion of the images and any portion of derived data in any form to any third party without [IOYS](http://ioys.co.kr/)’s prior written permission.

3. You agree **not to** further copy, publish, or distribute any portion of the Dataset. Except, for internal use at a single site within the same organization it is allowed to make copies of the Dataset.

4. [IOYS](http://ioys.co.kr/) reserves the right to terminate your access to the Dataset at any time.


### Download Instructions 

[SUBMISSION LINK](https://forms.gle/rVmcHCenChZx6jVV7)

The dataset is encrypted to prevent and track unauthorized access.

By requesting the link, you acknowledge that you have read the agreement, understand it, and agree to be bound by them. If you do not agree with these terms and conditions, you must not download and/or use the Dataset.

##### * We only approve a institution email adress. 
##### * Please do not reveal the URL to other people, and use the data according to the agreement.


### Data Explanation
The dataset contains 2,050 high-quality human scans captured by 80 multi-view DSLR cameras by [IOYS](http://ioys.co.kr/). CVTeam (KETI IIP Center) selected and post-processed the raw data to enable deep learning training and extract other information such as 3D pose, texture map, and parametric human model.

The dataset contains
- Train data
    * 2,000 of the 3D human models with vertex color (approximately 1M vertices)
    * 2,000 of low-resolution 3D human models with vertex color (approximately 50K vertices)
- Test data
    * 50 of the 3D human models with vertex color (100K vertices)
- Data loader
- Image rendering example: see the folder "source/"
- [Evaluation kit](https://github.com/SangHunHan92/2K2K)
- Parametric human model ([download](https://www.dropbox.com/scl/fi/ic3gpnz5ngr4lxquhyhyn/smplx.zip?rlkey=m1u2mfe0uvq5rz08si04jm0af&dl=0))
- The current SMPL-X parameters are initial estimates. We will update the parameters in both terms of quantity and quality. 
- 2K/3D Keypoints ([openpifpaf](https://github.com/openpifpaf/openpifpaf), [openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose))
  ([download](https://www.dropbox.com/scl/fi/6qb3a70nxjtug0lcxtrhc/keypoints.zip?rlkey=1f6rnacpfnipl3b0p9wx2z09v&dl=0))

<p align="center">
   <img src="./asset/00029.gif" width="20%" height="20%" /> <img src="./asset/00005.gif" width="20%" height="20%" /> <img src="./asset/00025.gif" width="20%" height="20%" /> <img src="./asset/00044.gif" width="20%" height="20%" />
</p>

We are also working on generating the following information, but it will take time.
- Unwrapped texture map (based on SMPL)
- UV texture map (xatlas)

  
### Citation
If you use this dataset for your research, please consider citing:
```
@InProceedings{han2023Recon2K,
title={High-fidelity 3D Human Digitization from Single 2K Resolution Images},
author={Han, Sang-Hun and Park, Min-Gyu and Yoon, Ju Hong and Kang, Ju-Mi and Park, Young-Jae and Jeon, Hae-Gon},
booktitle={IEEE Conference on Computer Vision and Pattern Recognition (CVPR2023)},
month={June},
year={2023},
}
```



### Contact for commercial use
- Ju Hong Yoon (jhyoon@keti.re.kr)



### Acknowledgment
- The work was partially supported by the Ministry of Trade, Industry and Energy (MOTIE) and Korea Institute for Advancement of Technology (KIAT) through the International Cooperative R&D program in part (P0019797), Institute of Information & Communications Technology Planning & Evaluation (IITP) grant (No.2021-0-02068, Artificial Intelligence Innovation Hub / No.2022-0-00566. The development of object media technology based on multiple video sources), GIST-MIT Research Collaboration, “Practical Research and Development support program supervised by the GTI(GIST Technology Institute)” funded by the GIST in 2023, ‘Project for Science and Technology Opens the Future of the Region’ program through the INNOPOLIS FOUNDATION funded by Ministry of Science and ICT, and the National Research Foundation of Korea (NRF) (No.2020R1C1C1012635) grant funded by the Korea government.
- Thanks to our collaborators, [WYSIWYG Studios Co.](http://www.wswgstudios.com/) and [UCSD Video Processing Lab](http://videoprocessing.ucsd.edu/), for discussion.
- We referenced [THuman 2.0 Dataset](https://github.com/ytrock/THuman2.0-Dataset) to create this page. Thanks to [Tao Yu](https://ytrock.com/) and [Prof. Yebin Liu](http://www.liuyebin.com/) for permission to use the terms and format of the THuman Dataset page.
