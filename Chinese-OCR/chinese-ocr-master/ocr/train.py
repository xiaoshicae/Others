import os

import numpy as np
from PIL import Image
from keras.callbacks import ModelCheckpoint

from alphabet import alphabet
from model import get_model


BASE_DIR = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))

imgH = 32
imgW = 256
n_len = 10
BATCH_SIZE = 32
nclass = len(alphabet)


def one_hot(text, length=10, characters=alphabet):
    label = np.zeros(length)
    for i, char in enumerate(text.decode('utf-8')):
        index = characters.find(char)
        if index == -1:
            index = characters.find(u' ')
        label[i] = index
    return label


def gen(loader, flag='train'):
    while True:
        i = 0
        n = len(loader)
        for X, Y in loader:
            X = X.numpy()
            X = X.reshape((-1, imgH, imgW, 1))
            if flag == 'test':
                Y = Y.numpy()

            Y = np.array(Y)
            Length = int(imgW / 4) - 1
            batchs = X.shape[0]
            # Y = Y.numpy()
            if i > n - 1:
                i = 0
                break

            yield [X, Y, np.ones(batchs) * int(Length), np.ones(batchs) * n_len], np.ones(batchs)


def train(model):
    img_train_folder = os.path.join(r'C:\Users\zhsh\Desktop\imgs', 'chinese-ocr')

    # callbacks 回调函数,用于记录过程量
    model_parameter = os.path.join(BASE_DIR, 'model_parameter', 'weights_first.{epoch:02d}.hdf5')
    check_pointer = ModelCheckpoint(filepath=model_parameter)
    # model.load_weights(os.path.join(BASE_DIR, 'model_parameter', 'ocr0.2.h5'))
    hist = model.fit_generator(
        generator=generate_arrays_from_img(img_train_folder),
        steps_per_epoch=10000,
        epochs=100,
        callbacks=[check_pointer],
    )

    # model.save('model.h5')

    loss = hist.history


def generate_arrays_from_img(folder):
    img_list = os.listdir(os.path.join(folder, 'train'))

    label_dict = {}
    with open(os.path.join(folder, 'labels.txt'), 'r', encoding='utf-8') as f:
        for line in f:
            line = line.replace('\n', '')
            k, v = line.split(', ')

            label_dict[k] = v

    print(label_dict)

    X = np.zeros((BATCH_SIZE, imgH, imgW, 1), dtype=np.uint8)
    Y = np.zeros((BATCH_SIZE, n_len), dtype=np.uint8)

    flag = 0
    length = len(img_list)
    while True:
        for i in range(BATCH_SIZE):
            index = int(flag % length)
            file_name = img_list[index]

            y_label = label_dict[file_name.split('.')[0]]
            img = os.path.join(folder, 'train', file_name)
            img_data = Image.open(img)
            img_data = img_data.convert('L')
            img_arr = np.array(img_data)
            # print(img_arr.shape)
            X[i] = img_arr.reshape(imgW, imgH, 1).transpose((1, 0, 2))
            Y[i] = [alphabet.find(x) for x in y_label]

            flag += 1

        yield [X, Y, np.ones(BATCH_SIZE) * int(int(imgW / 4) - 1),
               np.ones(BATCH_SIZE) * n_len], np.ones(BATCH_SIZE)


def main():
    model, base_model = get_model(imgH, nclass)
    train(model)


if __name__ == '__main__':
    main()
