# -*- coding: utf-8 -*-
import os
import dlib
# options用于设置训练的参数和模式
options = dlib.simple_object_detector_training_options()
# bool型，训练图像是否左右翻转，默认False
options.add_left_right_image_flips = True
# svm的C参数,默认为1
options.C = 10
# 训练的线程数目，默认4
options.num_threads = 6
# 训练终止误差，默认0.01
options.epsilon = 0.01
# 滑动窗口的大小，默认80*80
options.detection_window_size = 80*80
# bool型，是否在屏幕上输出训练过程中的日志信息，默认False
options.be_verbose = True
# 影像路徑
train_xml_path = os.getcwd() + '/data.xml'
# 開始訓練
dlib.train_simple_object_detector(train_xml_path, 'detector.svm', options)
# 顯示HOG特徵
detector = dlib.simple_object_detector("detector.svm")
win_det = dlib.image_window()
win_det.set_image(detector)
dlib.hit_enter_to_continue()
