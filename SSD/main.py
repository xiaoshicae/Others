#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 13:15
# @Email   : Zhuangshui@qiyi.com
# @Desc    :

import tensorflow as tf
import matplotlib.image as mpimg

from nets import ssd_vgg_300, np_methods
from preprocessing import ssd_vgg_preprocessing
from notebooks import visualization


def get_ssd_model_params(ckpt_filename):
    """获取ssd model"""

    slim = tf.contrib.slim

    # TensorFlow session: grow memory when needed. TF, DO NOT USE ALL MY GPU MEMORY!!!
    gpu_options = tf.GPUOptions(allow_growth=True)
    config = tf.ConfigProto(log_device_placement=False, gpu_options=gpu_options)
    isess = tf.InteractiveSession(config=config)

    # Input placeholder.
    net_shape = (300, 300)
    data_format = 'NHWC'
    img_input = tf.placeholder(tf.uint8, shape=(None, None, 3))
    # Evaluation pre-processing: resize to SSD net shape.
    image_pre, labels_pre, bboxes_pre, bbox_img = ssd_vgg_preprocessing.preprocess_for_eval(
        img_input, None, None, net_shape, data_format, resize=ssd_vgg_preprocessing.Resize.WARP_RESIZE)
    image_4d = tf.expand_dims(image_pre, 0)

    # Define the SSD model.
    reuse = True if 'ssd_net' in locals() else None
    ssd_net = ssd_vgg_300.SSDNet()
    with slim.arg_scope(ssd_net.arg_scope(data_format=data_format)):
        predictions, localisations, _, _ = ssd_net.net(image_4d, is_training=False, reuse=reuse)

    # Restore SSD model.
    isess.run(tf.global_variables_initializer())
    saver = tf.train.Saver()
    saver.restore(isess, ckpt_filename)

    # SSD default anchor boxes.
    ssd_anchors = ssd_net.anchors(net_shape)

    return {'isess': isess, 'image_4d': image_4d, 'predictions': predictions, 'localisations': localisations,
            'bbox_img': bbox_img, 'img_input': img_input, 'ssd_anchors': ssd_anchors}


def process_image(img, select_threshold=0.5, nms_threshold=.45, net_shape=(300, 300), model_params=None):
    """图片预处理"""
    # Run SSD network.
    isess = model_params['isess']
    image_4d = model_params['image_4d']
    predictions = model_params['predictions']
    localisations = model_params['localisations']
    bbox_img = model_params['bbox_img']
    img_input = model_params['img_input']
    ssd_anchors = model_params['ssd_anchors']

    rimg, rpredictions, rlocalisations, rbbox_img = isess.run([image_4d, predictions, localisations, bbox_img],
                                                              feed_dict={img_input: img})

    # Get classes and bboxes from the net outputs.
    rclasses, rscores, rbboxes = np_methods.ssd_bboxes_select(
        rpredictions, rlocalisations, ssd_anchors,
        select_threshold=select_threshold, img_shape=net_shape, num_classes=21, decode=True)

    rbboxes = np_methods.bboxes_clip(rbbox_img, rbboxes)
    rclasses, rscores, rbboxes = np_methods.bboxes_sort(rclasses, rscores, rbboxes, top_k=400)
    rclasses, rscores, rbboxes = np_methods.bboxes_nms(rclasses, rscores, rbboxes, nms_threshold=nms_threshold)
    rbboxes = np_methods.bboxes_resize(rbbox_img, rbboxes)
    return rclasses, rscores, rbboxes


def print_ssd_result(img_path):
    """打印ssd 检测结果"""

    img = mpimg.imread(img_path)

    ckpt_filename = r'/Users/zhuangshui/PycharmProjects/github/others/SSD/checkpoint/ssd_300_vgg.ckpt'
    model_params = get_ssd_model_params(ckpt_filename)

    rclasses, rscores, rbboxes = process_image(img, model_params=model_params)

    visualization.plt_bboxes(img, rclasses, rscores, rbboxes)


if __name__ == '__main__':
    img_path = r'/Users/zhuangshui/PycharmProjects/github/others/SSD/street.jpg'
    print_ssd_result(img_path)
