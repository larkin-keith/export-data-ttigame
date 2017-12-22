#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""配置类"""

__author__ = 'Lavenkin'

from enum import Enum

class Config(Enum):
	Mysql = {
		'host': '127.0.0.1',
		'user': 'root',
		'password': 'root',
		'db': 'appcenter'
	}
