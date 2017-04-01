#! /usr/bin/python
# -*- coding:utf-8 -*-  
# filename : testios.py
# author: hyper
# createdate: 2017/02/22

import sys
import wda
import random
import math
import time

def gesture(code):
	##点击事件
	if code == 0 or code == 2 or code == 4 or code == 6:
		session.tap(width*random.random(),height*random.random())
	##上滑动
	elif code == 1:
		swipe_width = width*random.random()
		if swipe_width < 100:
			swipe_width = 100
		swipe_height = width*random.random()
		if swipe_height < 100:
			swipe_height = 100
		session.swipe(swipe_width, swipe_height, swipe_width, swipe_height-100, 0.5)
	##下滑动	
	elif code == 3:
		swipe_width = width*random.random()
		if swipe_width < 100:
			swipe_width = 100
		swipe_height = width*random.random()
		if swipe_height < 100:
			swipe_height = 100
		session.swipe(swipe_width, swipe_height-100, swipe_width, swipe_height, 0.5)
	##左滑动
	elif code == 5:
		swipe_width = width*random.random()
		if swipe_width < 100:
			swipe_width = 100
		swipe_height = width*random.random()
		if swipe_height < 100:
			swipe_height = 100
		session.swipe(swipe_width-100, swipe_height, swipe_width, swipe_height, 0.5)
	##右滑动	
	elif code == 7:
		swipe_width = width*random.random()
		if swipe_width < 100:
			swipe_width = 100
		swipe_height = width*random.random()
		if swipe_height < 100:
			swipe_height = 100
		session.swipe(swipe_width, swipe_height, swipe_width-100, swipe_height, 0.5)

if __name__ == '__main__':
	bundleid = sys.argv[1]
	gesture_num = sys.argv[2]
	driver = wda.Client('http://localhost:8100')
	# 跳转Safari
	session = driver.session(bundleid)
	# 取得屏幕大小
	height = session.window_size().height
	width = session.window_size().width
	#session.tap(20,30)
	#session.swipe(300, 400, 300, 100, 1.0)
	#等待60s，用户进行初始化操作
	time.sleep(60)
	num = int(gesture_num)
	while num>0 :
		num = num -1
		code = math.floor(random.random()*8)
		gesture(code)