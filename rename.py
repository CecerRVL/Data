import os

path = os.getcwd() + '/20191116data_augmentation/normal/'
all_name = os.listdir(path)
all_name.sort(key= lambda x:int(x[:-4]))

n = 0

for i in all_name:
    name = str(n) + '.png'
    # name = 'u' + i
    if '.png' in i:          
        os.rename(path + i , path + name)
        n = n+1

