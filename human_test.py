import os
import numpy as np
import cv2

path = os.getcwd() + '/new_testdata_human/'
all_name = os.listdir(path)
np.random.shuffle(all_name)
print(all_name)

crash = 0
dirty = 0
normal = 0
uneven = 0
total = 0

for i in all_name:
    image = cv2.imread(path + i)
    image = cv2.resize(image, (1280,720))
    cv2.imshow('Test', image)
    k = cv2.waitKey(0)
    if(k == ord('c')):
        if(i[0] == 'c'):
            crash+=1
            total+=1
    elif(k == ord('d')):
        if(i[0] == 'd'):
            dirty+=1
            total+=1
    elif(k == ord('n')):
        if(i[0] == 'n'):
            normal+=1
            total+=1
    elif(k == ord('u')):
        if(i[0] == 'u'):
            uneven+=1
            total+=1
    elif(k == ord('q')):
        break

print('crash accuracy = {}%'.format(crash*10))
print('dirty accuracy = {}%'.format(dirty*10))
print('normal accuracy = {}%'.format(normal*10))
print('uneven accuracy = {}%'.format(uneven*10))
print('total accuracy = {}%'.format(total*2.5))
