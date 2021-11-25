import os
import glob
import shutil
import natsort
import random

img_path = 'train'
images = glob.glob(img_path + '/*.png')  # 載入所有 jpg 檔成為一個 list
# filenames = (next(os.walk(img_path), (None, None, []))[2])  # [] if no file
# filenames = natsort.natsorted(filenames)
images = natsort.natsorted(images)
filenames = [images[i].split('/')[-1].replace('.png','.txt') for i in range(len(images)) ]
print(images[0:5], filenames[0:5])
print(f"len(images): {len(images)}, len(filenames): {len(filenames)}")  # 印出單一類別有幾張圖片
num_train = int(round(len(images)*0.8))  # 切割 80% 資料作為訓練集
train_img, train_filename  = images[:num_train], filenames[:num_train]
valid_img, valid_filename  = images[num_train:], filenames[num_train:]
print('train: {}, valid: {}' .format(len(train_filename), len(valid_filename)))

# # Random split
# indices = list(range(len(images)))
# random.shuffle(indices)
# train_idx, valid_idx = indices[:num_train], indices[num_train:]
# train = [images[i] for i in train_idx]
# valid = [images[i] for i in valid_idx]

basefolder = 'svhn'

if not os.path.exists(os.path.join(basefolder, 'train')):  # 資料夾不存在
    os.makedirs(os.path.join(basefolder, 'train'))  # 建立新資料夾
if not os.path.exists(os.path.join(basefolder, 'valid')):  # 如果資料夾不存在
    os.makedirs(os.path.join(basefolder, 'valid'))  # 建立新資料夾

for im, fn in zip(train_img, train_filename):
    shutil.copy(im, os.path.join(basefolder, 'train'))  # 搬運圖片資料到新的資料夾
    shutil.copy(os.path.join('train/labels', fn), os.path.join(basefolder, 'train'))
    print('({}, {}) 2 {}' .format(im, fn, os.path.join(basefolder, 'train')))
for im, fn in zip(valid_img, valid_filename):
    shutil.copy(im, os.path.join(basefolder, 'valid'))
    shutil.copy(os.path.join('train/labels', fn), os.path.join(basefolder, 'valid'))
    print('({}, {}) 2 {}' .format(im, fn, os.path.join(basefolder, 'valid')))

print('train: {}, valid: {}' .format(len(train_filename), len(valid_filename)))

# shutil.rmtree('./train')
# print('./train delete!')