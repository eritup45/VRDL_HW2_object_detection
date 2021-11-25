import enum
import os
import cv2
import json
import glob
import natsort

test_image_path = 'data/svhn/test/'
filepath = 'runs/detect/exp26_x_320/labels/'
filenames = natsort.natsorted(glob.glob(filepath + '/*.txt'))
fileIDs = [int((f.split('/')[-1])[:-4]) for f in filenames]
length = len(fileIDs)

# print(fileIDs)
# print(length)


data = []
# for i in range(1, length):
for i, (id, filename) in enumerate(zip(fileIDs, filenames)):
    f = open(filename, 'r')
    contents = f.readlines()

    im = cv2.imread(test_image_path + str(id) + '.png')
    h, w, c = im.shape
    # print(h,w)

    for content in contents:
        a = {"image_id": id, "bbox": [], "score": 0, "category_id": 0}
        content = content.replace('\n', '')
        c = content.split(' ')

        w_center = w * float(c[1])
        h_center = h * float(c[2])
        width = w * float(c[3])
        height = h * float(c[4])
        left = int(w_center - width/2)
        top = int(h_center - height/2)
        # right = int(w_center + width/2)
        # bottom = int(h_center + height/2)

        category_id = int(c[0])
        # bbox = [top, left, width, height]
        bbox = [left, top, width, height]  # better acc
        score = float(c[5])
        a["bbox"] = bbox
        a['score'] = score
        a["category_id"] = category_id
        print(a)
        data.append(a)

    f.close()

ret = json.dumps(data)

print(len(data))
with open('answer.json', 'w') as fp:
    fp.write(ret)
