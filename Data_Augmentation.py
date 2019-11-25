import os
from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator

path = os.getcwd() + '/newdata/normal/'
all_name = os.listdir(path)
all_name.sort(key= lambda x:int(x[:-4]))

for j in all_name:

    print(j)
    img = load_img(path + j)
    data = img_to_array(img)

    # expand dimension to one sample
    samples = expand_dims(data, 0)

    datagen = ImageDataGenerator(
        horizontal_flip=True,
        vertical_flip=True,
        rotation_range=90,
        fill_mode='reflect',
        # fill_mode='wrap',
        # fill_mode='nearest',
        width_shift_range = 0.3,
        height_shift_range = 0.3,
        shear_range=45.0,
        zoom_range=[0.5,1.0]
    )
    it = datagen.flow(samples, batch_size=1, save_to_dir='Data_Augmentation', save_format='png')
    for i in range(1):
        batch = it.next()
        # k = input("Press enter key to continue...")


