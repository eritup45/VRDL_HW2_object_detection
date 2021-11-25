# VRDL_HW2_object_detection

### Objective
Object detection of street view house numbers, which contains two parts:
1. Do bounding box regression to find top, left, width and height of bounding boxes which contain digits in a given image
2. classify the digits of bounding boxes into 10 classes (0-9)

The giving SVHN dataset contains 33402 images for training and 13068 images for testing. This project uses the YOLOv5 pre-trained model to detect the number.

### Environment
- Python 3.7
- Pytorch 1.6.0
- CUDA 10.2

## Reproducing Submission
To reproduce, do the following steps:
1. [Installation](#install-packages)
2. [Data Preparation](#data-preparation)
3. [Set Configuration](#set-configuration)
4. [Download Pretrained Model](#download-pretrained-model)
5. [Training](#training)
6. [Testing](#testing)
7. [Results](#results)
8. [Report](#report)
9. [Reference](#reference)



### Install Packages
- install pytorch from https://pytorch.org/get-started/previous-versions/

- install dependencies
```
pip install -r requirements.txt
```

### Data Preparation
* Recommend Way
  1. Download dataset which has been preprocessed. [Google Drive](https://drive.google.com/drive/folders/1qEDem8pauW_r7wfrRB9sA9wmfSOag8pf?usp=sharing). The data should be as follow.
  ```
  data
  └── svhn
      ├── train
      │   ├── 1.png
      │   ├── 1.txt
      │   ├── 2.png
      │   ├── 2.txt
      │   └── ...
      ├── val
      │   ├── 1.png
      │   ├── 1.txt
      │   ├── 2.png
      │   ├── 2.txt
      │   └── ...
      └── test
          ├── 1.jpg
          ├── 2.jpg
          └── ...
  ```


* Or, Prepare Data From Scratch
  1. Download the given dataset from [Google Drive](https://drive.google.com/drive/folders/1I3gEXFGE1ERu6nbvB-ON7zcsXze0NgmC?usp=sharing).
  ```
  data/
    +- svhn/
    +- train/
    |	+- xxx.jpg
    |	+- digitStruct.mat
    +- test/
    |	+- yyy.jpg
    +- mat_to_yolo.py
    +- shvn.yaml
  ```
  2. Run command `python mat_to_yolo.py` to create labels for yolo and reorganize the train data structure as below:
  ```
  - train/
  ├── 1.png
  ├── 1.txt
  ├── 2.png
  ├── 2.txt
  │     .
  │     .
  │     .
  ├── 33402.png
  └── 33402.txt
  ```
  3. Run command `python split_train_val.py` to split data into train and valid folder. The results will be stored in "./data/svhn/". (Optional: copy "./data/test/" to "./data/svhn/")

### Set Configuration
- create `svhn.yaml` in `./data`
```
train: data/svhn/train  # 33402 images
val: data/svhn/valid  # 3000 images

# number of classes
nc: 10

# class names
names: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
```

### Download Pretrained Model
- https://github.com/ultralytics/yolov5/releases

### Training
- train model with pretrained model
```
python train.py --img 320 --batch 32 --epochs 80 --data svhn.yaml --weights yolov5m.pt
```

### Testing
- detect test data
```
python detect.py --source data/svhn/test/ --weights runs/train/exp18/weights/best.pt --conf 0.005 --save-txt --save-conf
```

- Make Submission: output json format. The result will be stored in "./answer.json". (Modify combine.py corresponding to your detect labels.)
```
python combine.py
```

- Format of "./answer.json" is same as COCO results.
```
[{
  "image_id": id,
  "bbox": [left, top, width, height],
  "score": confidence,
  "category_id": class
 },
 {"image_id": 499877, "bbox": [263, 74, 10.999989, 18.000008], "score": 0.614746, "category_id": 9}
]
```

### Results
Test score (mAP:0.5:0.95): 0.38221 (60)

### Report
https://hackmd.io/@Bmj6Z_QbTMy769jUvLGShA/VRDL_HW2

### Reference
- [Street-View-House-Numbers-Detection](https://github.com/chia56028/Street-View-House-Numbers-Detection)
- [h5py - Quick Start Guide](https://docs.h5py.org/en/stable/quick.html)
- [YOLOv5](https://github.com/ultralytics/yolov5)