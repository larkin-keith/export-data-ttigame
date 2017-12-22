#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""获取结果并导出到Excel"""

__author__ = 'Lavenkin'

import os

from Config import *
from FormatTxt import *
from ConnectDb import *

class ExportRes(object):

	def __init__(self, host, user, password, db, table, select):
		self._host = host
		self._user = user
		self._password = password
		self._db = db
		self._table = table
		self._select = select

	def __getIds(self):
		formatTxt = FormatTxt()
		print('%s/file/format.txt' % (os.getcwd()))
		formatTxt.getFilePath('%s/file/id.txt' % (os.getcwd())).fileOpen().move('%s/file/format.txt' % (os.getcwd()))
		with open('%s/file/format.txt' % (os.getcwd()), 'r') as f:
			return f.read()

	def __getRes(self):
		connectDb = ConnectDb(self._host, self._user, self._password, self._db)
		return connectDb.connect().table(self._table).select(self._select).whereIn('id', self.__getIds()).get()

	def exportExcel(self):
		print(self.__getRes())

if __name__ == '__main__':
	mysql = Config.Mysql.value
	host = mysql['host']
	user = mysql['user']
	password = mysql['password']
	db = mysql['db']

	table = input('please enter you whant search table: ')
	fields = input('please enter you whant search fields: ')

	e = ExportRes(host, user, password, db, table, fields)
	e.exportExcel()