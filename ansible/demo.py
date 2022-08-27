#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : skylens
# @Time     : 2022/8/26 21:43


import ansible_runner

m = ansible_runner.run(inventory="inventory",quiet=True,json_mode=True,private_data_dir = './tmp', host_pattern = 'all', module = 'ping')
# print("{}: {}".format(m.status, m.rc))

print(m.stdout)