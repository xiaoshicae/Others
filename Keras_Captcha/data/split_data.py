import os
import random
import shutil


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def split_data():
    image_list = os.listdir(os.path.join(BASE_DIR, 'origin_images'))
    image_list.remove('error')

    random.shuffle(image_list)

    length = len(image_list)
    cut_point = int(length/10*9)

    train_list = image_list[:cut_point]
    test_list = image_list[cut_point:]

    for i in train_list:
        shutil.copy(os.path.join(BASE_DIR, 'origin_images',  i), os.path.join(BASE_DIR, 'data', 'train', i))
        print(i, ' has been copied to train data')

    for j in test_list:
        shutil.copy(os.path.join(BASE_DIR, 'origin_images',  j), os.path.join(BASE_DIR, 'data', 'test', j))
        print(j, ' has been copied to test data')

    print('down!')


if __name__ == '__main__':
    # split_data()
    print(BASE_DIR)
