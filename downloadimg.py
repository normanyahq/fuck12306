#!/usr/bin/python
# #  FileName    : fuck12306.py
# #  Author      : MaoMaog Wang <andelf@gmail.com>
# #  Created     : Mon Mar 16 22:08:41 2015 by ShuYu Wang
# #  Copyright   : Feather (c) 2015
# #  Description : fuck fuck 12306
# #  Time-stamp: <2015-03-16 22:12:31 andelf>


#from PIL import Image
import urllib
import urllib2
import re
import json
import os
import datetime
import random
# hack CERTIFICATE_VERIFY_FAILED
# https://github.com/mtschirs/quizduellapi/issues/2
import ssl
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context


UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36"

pic_url = "https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=login&rand=sjrand&0.%d"


def valid_image(raw_data):
    print raw_data
    return False if len(raw_data) < 1500 or "</html>" in raw_data else True

def get_img(dirname="download", filename="tmp.jpg"):
    resp = urllib2.urlopen(pic_url % (random.randrange(10**18, 10**19)), timeout=10)
    raw = resp.read()
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    print ("image size:%d"%len(raw))
    if not valid_image(raw):
        print ("invalid image")
        return False
    with open(os.path.join(dirname, filename), 'wb') as fp:
        fp.write(raw)
    return True


if __name__ == '__main__':
    image_count = 0
    while image_count < 100000:
        if os.path.exists(os.path.join("download", str(image_count+1)+".jpg")):
            image_count += 1
            continue
        try:
            print ("getting image: %d, %s" % (image_count, datetime.datetime.now()))
            if get_img("download", str(image_count+1)+".jpg"):
                image_count += 1
        except IOError:
            print ("failed to get image.")
            pass
