# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Description :
   Author :       kinredon
   date：          2019/3/25
-------------------------------------------------
"""
from humanseg import Humanseg

image_path = 'img/xixi.jpg'
output_path = '.'.join(image_path.split('.')[0:-1]) + '_seg.{}'.format(image_path.split('.')[-1])
print(output_path)
hs = Humanseg()
time = hs.seg(image_path, output_path)
print('time used : %d sec' % time)

