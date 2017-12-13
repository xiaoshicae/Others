# --*-- coding: utf-8 --*--
import importlib
import os
import time
import numpy as np
import keras.backend as K
from PIL import Image


from . import config
from . import model as keras_model
model_module = keras_model
config_module = config


def decode(y):
    characters = config_module.CHARACTERS + ' '
    y = np.argmax(np.array(y), axis=2)[:, 0]
    return ''.join([characters[x] for x in y])


def predict(model, img_data):
    model.load_weights(r'C:\Users\YongHu\Desktop\TMP\model_parameter\weights_first.23.hdf5')
    characters2 = config_module.CHARACTERS + ' '

    X = img_data
    X = np.expand_dims(X, 0)

    y_pred = model.predict(X)
    y_pred = y_pred[:, 2:, :]
    out = K.get_value(K.ctc_decode(y_pred, input_length=np.ones(y_pred.shape[0]) * y_pred.shape[1], )[0][0])[:, :4]
    out = ''.join([characters2[x] for x in out[0]])
    return out


def main(img):
    base_model, model = model_module.model()
    img_data = Image.open(img)
    # img_data.resize((80, 170))
    img_data = np.array(img_data).transpose((1, 0, 2))
    # out = predict(model, img_data)
    out2 = predict(base_model, img_data)
    return out2


if __name__ == '__main__':
    r = main(r'C:\Users\YongHu\Desktop\Flask_App\ZhifubaoRegisterVerify\app\script\images\2ABU_abeb7912-d5af-11e7-ae6a-dc4a3e8b7c67.png')
    print(r)

