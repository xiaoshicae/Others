# --*-- coding:UTF-8 --*--
import os

import numpy as np
from PIL import Image, ImageFont, ImageDraw

from alphabet import get_text


folder = r'C:\Users\zhsh\Desktop\imgs\chinese-ocr'


def gen_img(n):
    text = ''.join([get_text() for i in range(n)])

    w, h = 256, 32
    img = Image.new('RGB', (w, h), (255, 255, 255))
    font = ImageFont.truetype(r'./STSONG.ttf', 25)
    draw = ImageDraw.Draw(img)
    draw.text((2, -1), text, fill=(0, 0, 0), font=font)
    return img, text


def gen_data():
    f = open(os.path.join(folder, 'labels.txt'), 'a', encoding='utf-8')
    f.write('图片名称, 图片内容\n')
    # for i in range(100000):
    #     img, text = gen_img(10)
    #     f.write(str(i) + ', ' + text + '\n')
    #     img.save(os.path.join(folder,  'train', '%s.jpg' % str(i)))

    for j in range(100000, 110000):
        img, text = gen_img(10)
        f.write(str(j) + ', ' + text + '\n')
        img.save(os.path.join(folder, 'val', '%s.jpg' % str(j)))


if __name__ == '__main__':
    gen_data()
