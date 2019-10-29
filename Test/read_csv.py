#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import choice
userdata = []
with open('../Data/userdata.csv') as f:
	for line in f.readlines():
		# print(line)
		userdata.append(line.strip())
		userinfo = choice(userdata)
		userinfo = userinfo.split(',')
		username  = userinfo[0]
		print(username)
		pwd = userinfo[1]
		print(pwd)