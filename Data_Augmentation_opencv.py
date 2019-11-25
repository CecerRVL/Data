import os
import cv2

path = os.getcwd() + '/20191116data_augmentation/uneven/'
all_name = os.listdir(path)
all_name.sort(key= lambda x:int(x[:-4]))

n = 224

for j in all_name:
    print(j)
    image = cv2.imread(path + j)

    image_change = cv2.flip(image, 1)
    # image_change = cv2.flip(image, 0)

    path_name = path + str(n) + '.png'
    cv2.imwrite( path_name, image_change)
    n += 1