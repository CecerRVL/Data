import os
import cv2

path = os.getcwd() + '/Data_Augmentation/'
all_name = os.listdir(path)
# all_name.sort(key= lambda x:str(x[:-4]))

n = 1042
for i in all_name:
    name = str(n) + '.png'

    if '.png' in i:
        img = cv2.imread(path + i)
        img = cv2.resize(img,(1280,720))
        cv2.imshow( i, img)
        k = cv2.waitKey(0)
        if(k == ord('s')):
            os.rename(path + i , path + name)
            n = n+1
            cv2.destroyWindow(i)
        elif(k == ord('d')):
            os.remove(path + i)
            cv2.destroyWindow(i)
        elif(k == ord('q')):
            break

cv2.destroyAllWindows()