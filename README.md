# 2K2K Dataset
### High-fidelity 3D Human Digitization from Single 2K Resolution Images
Sang-Hun Han, [Min-Gyu Park](https://scholar.google.co.uk/citations?user=VUj1ZWoAAAAJ&hl=en), [Ju Hong Yoon](https://scholar.google.com/citations?user=Y4mReV4AAAAJ&hl=en), Ju-Mi Kang, Young-Jae Park and [Hae-Gon Jeon](https://sites.google.com/site/hgjeoncv/).  CVPR 2023

[[Project Page]](https://github.com/SangHunHan92/2K2K)



### Agreement
1. The 2K2K dataset (the "Dataset") is available for **non-commercial** research purposes only. Any other use, in particular any use for commercial purposes, is prohibited. This includes, without limitation, incorporation in a commercial product, use in a commercial service, as training data for a commercial product, for commercial ergonomic analysis (e.g. product design, architectural design, etc.), or production of other artifacts for commercial purposes including, for example, web services, movies, television programs, mobile applications, or video games. The dataset may not be used for pornographic purposes or to generate pornographic material whether commercial or not. The Dataset may not be reproduced, modified and/or made available in any form to any third party without [IOYS](http://ioys.co.kr/)’s prior written permission.

2. You agree **not to** reproduce, modified, duplicate, copy, sell, trade, resell or exploit any portion of the images and any portion of derived data in any form to any third party without [IOYS](http://ioys.co.kr/)’s prior written permission.

3. You agree **not to** further copy, publish or distribute any portion of the Dataset. Except, for internal use at a single site within the same organization it is allowed to make copies of the dataset.

4. [IOYS](http://ioys.co.kr/) reserve the right to terminate your access to the Dataset at any time.



### Download Instructions 
Dataset is encrypted to prevent unauthorized access.

Please fill the [request form](./2K2K_Agreement.pdf) and send it to the manager (khuman23@gmail.com).

By requesting for the link, you acknowledge that you have read the agreement, understand it, and agree to be bound by them. If you do not agree with these terms and conditions, you must not download and/or use the Dataset.



### Data Explanation
Dataset contains 2,040 high-quality human scans captured by 80 multi-view DSLR cameras by [IOYS](http://ioys.co.kr/), and KetiVision and [GIST Visual AI Lab](https://sites.google.com/site/hgjeoncv/) selected and post-processed the raw data to enable deep learning training and extract other information such as 3D pose, texture map, and paramteric human model.
The dataset contains
- 3D human model (approximately 1M vertices and 2M faces)
- Texture map (jpg)
- 3D Pose ([openpifpaf](https://github.com/openpifpaf/openpifpaf), [openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose))
- Parameteric human model ([SMPLX](https://smpl.is.tue.mpg.de/))
- Evaluation and image rendering kit



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



### Contact
- Ju Hong Yoon / Min-Gyu Park [(khuman23@gmail.com)](mailto:khuman23@gmail.com)



### Acknowledgment
- This work was equally supported by Korea Institute for Advancement of Technology(KIAT) grant funded by the Korea Government(MOTIE)(P146500035, The development of interactive metaverse concert solutions via neural human modeling) and by Institute of Information & communications Technology Planning & Evaluation (IITP) grant funded by the Korea government(MSIT) (No. 2022-0-00566. The development of object media technology based on multiple video sources).
- Thanks to our collaborators, [WYSIWYG Studios Co.](http://www.wswgstudios.com/) and [UCSD Video Processing Lab](http://videoprocessing.ucsd.edu/), for discussion.
- We referenced [THuman 2.0 Dataset](https://github.com/ytrock/THuman2.0-Dataset) to create this page. Thanks to [Tao Yu](https://ytrock.com/) and [Prof. Yebin Liu](http://www.liuyebin.com/) for permission to use the terms and format of the THuman page.
