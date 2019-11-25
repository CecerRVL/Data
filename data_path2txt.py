# encoding: UTF-8

import os
import re

def createFileList(images_path, txt_save_path):
    fw = open(txt_save_path, "w")
    images_name = os.listdir(images_path)
    images_name.sort(key= lambda x:int(x[:-4]))
    for eachname in images_name:
        fw.write( images_path+ eachname+ '\n')
    print("生成txt檔案成功")
    fw.close()

if __name__ == '__main__':

    txt_path = os.getcwd()
    print(txt_path)
    images_path = txt_path + '/'+ 'data/'
    txt_name = 'data_path_list.txt'
    txt_save_path = txt_path + '/'+ txt_name
    createFileList(images_path, txt_save_path)