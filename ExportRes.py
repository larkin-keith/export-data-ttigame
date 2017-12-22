#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""获取结果并导出到Excel"""

__author__ = 'Lavenkin'

import os

from FormatTxt import *
from ConnectDb import *
from openpyxl import Workbook

class ExportRes(object):

	def __init__(self, table, status, select):
		self._table = table
		self._status = status
		self._select = select

	def __getIds(self):
		formatTxt = FormatTxt()
		print('%s/file/format.txt' % (os.getcwd()))
		formatTxt.getFilePath('%s/file/id.txt' % (os.getcwd())).fileOpen().move('%s/file/format.txt' % (os.getcwd()))
		with open('%s/file/format.txt' % (os.getcwd()), 'r') as f:
			return f.read()

	def __getRes(self):
		connectDb = ConnectDb()
		res = connectDb.connect().table(self._table).select(self._select).where('release_status', '=', self._status).whereIn('id', self.__getIds()).get()
		connectDb.close()
		return res

	def exportExcel(self):
		print('正在导出Excel文档请稍等...')
		wb = Workbook()
		sheet = wb.active
		for value in self.__getRes():
			sheet.append(value)

		wb.save('%s/file/export.xlsx' % (os.getcwd()))
		print('文件导出成功，请在./file目录下查看导出文档')

if __name__ == '__main__':

	table = input('please enter you want to search table (like games_view or softwares_view): ')
	status = input('please enter you want to display status (like show or hide): ')
	fields = input('please enter you want to search fields (like id, name, level): ')

	e = ExportRes(table, status, fields)
	e.exportExcel()