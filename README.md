创意idea、深度学习练习
===

[![Travis](https://img.shields.io/travis/gothinkster/realworld.svg)](https://travis-ci.org/gothinkster/realworld)

简介:
1. 一些idea、练习 <br>

2. 深度学习目前片图像识别方向(验证码识别、目标探测) <br>

3. 脚本具体技术栈,及代码详解可以参考[博客](http://101.132.152.66/blog "阿里云Blog")  

---

## 目录
    
* ### KerasCaptcha(Keras验证码破解)
    * Keras cnn+rnn模型
    * 第三方接口标记初始样本(约2W张)
    * 识别率90%以上

* ### SSD(TensorFlow目标检测)
    * 基于TensorFlow
    * 常用的目标检测有:rnn、faster-rnn、yolo、ssd等(ssd比faster-rnn效率高、比yolo准确率高);
    * 检测出图片中的人、车、椅子等特定物体
    * 基于该模型可以改造成识别文字位置

## License
[Apache License 2.0](LICENSE)
