# -*- coding: utf-8 -*-
import os
import dlib
# 顯示HOG特徵
detector = dlib.simple_object_detector("detector.svm")
win_det = dlib.image_window()
win_det.set_image(detector)
dlib.hit_enter_to_continue()