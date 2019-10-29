#!/usr/bin/env python
# -*- coding: utf-8 -*-
from locust import HttpLocust,task,TaskSet
from random import choice
class DiscLogin(TaskSet):
	'''登录业务类'''
	def __login(self):
		'''登录'''
		userinfo = choice(self.locust.userdata)
		userinfo = userinfo.split(',')
		username  = userinfo[0]
		pwd = userinfo[1]
		url= '/video_analysis/user/login'
		headers ={ "Accept": "application/json, text/plain, */*",
					"Accept-Encoding": "gzip, deflate",
					"Accept-Language": "zh-CN,zh;q=0.9",
					"Connection": "keep-alive",
					"Content-Length": "39",
					"Content-Type": "application/x-www-form-urlencoded",
					"Host": "10.168.103.151",
					"Origin": "http://10.168.103.151",
					"Referer": "http://10.168.103.151/",
					"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
		data = {	"username": "admin:" + username,
					"password": pwd}
		print(data)
		with self.client.post(url,headers=headers,data=data,name='登录') as response:
			json_res = response.json()
			print('-------------',json_res)
			assert '所有权限' in json_res
			return json_res

	def get_token(self):
		token = self.__login()['token']
		print(token)

	def logout(self):
		'''退出'''
		url = ('/video_analysis/user/exit')
		self.client.get(url)

class DiscUser(HttpLocust):
	'''用户类'''
	task_set = DiscLogin
	min_wait = 3000
	max_wait = 5000
	host = 'http://10.168.103.151'

	userdata = []
	with open('../Data/userdata.csv') as f:
		for line in f.readlines():
			userdata.append(line.strip())


