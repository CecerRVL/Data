import os
import cv2
from shutil import move

path = os.getcwd() + '/newdata2-1/uneven/'
all_name = os.listdir(path)
all_name.sort(key= lambda x:int(x[:-4]))
dst_path = os.getcwd() + '/newdata2'

for i in all_name:

    if '.png' in i:
        img = cv2.imread(path + i)
        img = cv2.resize(img,(1280,720))
        cv2.imshow( i, img)
        k = cv2.waitKey(0)
        if(k == ord('c')):
            move(path + i , dst_path + '/crash/')
            cv2.destroyWindow(i)
        elif(k == ord('d')):
            move(path + i , dst_path + '/dirty/')
            cv2.destroyWindow(i)
        elif(k == ord('n')):
            move(path + i , dst_path + '/normal/')
            cv2.destroyWindow(i)
        elif(k == ord('u')):
            move(path + i , dst_path + '/uneven/')
            cv2.destroyWindow(i)
        elif(k == ord('x')):
            os.remove(path + i)
            cv2.destroyWindow(i)
        elif(k == ord('q')):
            break

cv2.destroyAllWindows()