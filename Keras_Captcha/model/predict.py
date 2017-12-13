# --*-- coding: utf-8 --*--
import importlib
import os
import time
import numpy as np
import keras.backend as K
from PIL import Image


model_module = importlib.import_module('model')
config_module = importlib.import_module('config')


def decode(y):
    characters = config_module.CHARACTERS + ' '
    y = np.argmax(np.array(y), axis=2)[:, 0]
    return ''.join([characters[x] for x in y])


def predict(model, img_data):
    model.load_weights(os.path.join(config_module.BASE_DIR, 'model_parameter', 'weights_first.7.hdf5'))
    characters2 = config_module.CHARACTERS + ' '

    X = img_data
    X = np.expand_dims(X, 0)

    y_pred = model.predict(X)
    y_pred = y_pred[:, 2:, :]
    out = K.get_value(K.ctc_decode(y_pred, input_length=np.ones(y_pred.shape[0]) * y_pred.shape[1], )[0][0])[:, :4]
    out = ''.join([characters2[x] for x in out[0]])
    print('y_pred: %s' % out)

    return out


def main(img):
    base_model, model = model_module.model()
    img_data = Image.open(img)
    # img_data.resize((80, 170))
    img_data = np.array(img_data).transpose((1, 0, 2))
    # out = predict(model, img_data)
    out2 = predict(base_model, img_data)
    return out2


def verify(times):
    characters2 = config_module.CHARACTERS + ' '
    base_model, model = model_module.model()
    # base_model.load_weights(r'C:\Users\YongHu\Desktop\TMP\model_parameter\weights_firts_d.%s.hdf5' % str(times).zfill(2))
    base_model.load_weights(r'C:\Users\YongHu\Desktop\TMP\p2\weights_firts_c.%s.hdf5' % str(times).zfill(2))

    folder = r'C:\Users\YongHu\Desktop\TMP\data\test2'
    img_list = os.listdir(folder)

    count = 0
    ttl = 0
    begin = time.time()
    for i in img_list:
        ttl += 1
        y_true = i.split('_')[0]

        img = os.path.join(folder, i)
        img_data = Image.open(img)
        img_data = np.array(img_data).transpose((1, 0, 2))
        X = img_data
        X = np.expand_dims(X, 0)
        y_pred = base_model.predict(X)
        y_pred = y_pred[:, 2:, :]
        out = K.get_value(K.ctc_decode(y_pred, input_length=np.ones(y_pred.shape[0]) * y_pred.shape[1], )[0][0])[:, :4]
        y_predict = ''.join([characters2[x] for x in out[0]])

        if y_predict.lower() == y_true.lower():
            count += 1
            print('count: 【%s】, ttl: 【%s】, 正确率: 【%s】' % (str(count), str(ttl), str(count / ttl)))
        else:
            print('img【%s】error, y_true: 【%s】, y_predict: 【%s】' % (i, y_true, y_predict))

    print('正确率为: %s' % str(count / ttl))
    print('共花费【%s】秒' % str(time.time()-begin))
    del base_model, model
    return {'times': times, 'accuracy': count / ttl}

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('-t', '--times', type=int, default=1)  # 输入其实轮次
    args = parser.parse_args()
    times = int(args.times)

    import json
    f = open('accuracy_d.log', 'a', encoding='utf-8')
    for i in range(70, 91):
        r = verify(i)
        print(r)
        f.write(json.dumps(r)+'\n')
        f.flush()
    f.close()
    print('down!...')
