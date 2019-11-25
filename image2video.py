import cv2
import os

path = os.getcwd() + '/Test/test2_pred/'
all_name = os.listdir(path)
all_name.sort(key= lambda x:int(x[:-4]))

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

out = cv2.VideoWriter('2080Ti_2class_demo2.mp4', fourcc, 8.0, (1920, 1200))

for i in all_name:
    image = cv2.imread(path + i)
    out.write(image)

out.release()
