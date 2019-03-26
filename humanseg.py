# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Description :
   Author :       kinredon
   date：          2019/3/26
-------------------------------------------------
-------------------------------------------------
                    Usage
-------------------------------------------------
here we have provide an example:

    from humanseg import Humanseg

    image_path = '/PATH/TO/IMAGE'
    output_path = '.'.join(image_path.split('.')[0:-1]) + '_seg.{}'.format(image_path.split('.')[-1])
    print(output_path)
    hs = Humanseg()
    time = hs.seg(image_path, output_path)

"""
import requests
import base64
import simplejson as json
import time


class Humanseg():

    def __init__(self, api_key='DocKgzKbalKRPLEW_HVhqf1hivmtD9gX', api_secret = 'vTAnUYZq5_tNAo18547t6iBmHHtXisfX'):
        '''
        Init some variables for human seg
        :param api_key: face++ api key
        :param api_secret: face++ api secret
        '''
        # request headers
        self.headers = {
            "Host": "youpin.mi.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "https://api-cn.faceplusplus.com/",  # 必须带这个参数，不然会报错
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
        }
        # request url
        self.url = "https://api-cn.faceplusplus.com/humanbodypp/v2/segment"
        self.api_key = api_key
        self.api_secret = api_secret

    def seg(self, image_path, output_path):
        '''
        main function: human segmentation.
        :param image_path: the path of image that segment
        :param output_path: the path of segment result
        :return: total used time. unit second
        '''
        start_time = time.time()
        with open(image_path, 'rb') as f:
            data = f.read()
            encodestr = base64.b64encode(data)
        form_data = {'api_key': self.api_key,
                     'api_secret': self.api_secret,
                     'image_base64': encodestr,
                     'return_grayscale': 0}
        # post request
        results = requests.post(self.url, data=form_data, headers=self.headers)
        # result content, json format
        content = json.loads(results.text)
        body_image = content['body_image']
        imgdata = base64.b64decode(body_image)
        with open(output_path, 'wb') as f:
            f.write(imgdata)
        end_time = time.time()

        return end_time - start_time

