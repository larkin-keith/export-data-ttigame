#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""webhook for hexo blog"""

__author__ = 'Lavenkin'

import os

class FormatTxt(object):

	def getFilePath(self, path):
		self._filePath = path
		return self

	def fileOpen(self):
		try:
			with open(self._filePath, encoding = 'utf-8') as f:
				self._content = []
				for line in f.readlines():
					self._content.append(line.strip())

			return self
		except Exception as e:
			print(e)

	def move(self, newfile):
		if os.path.exists(newfile):
			os.remove(newfile)
		# print(newfile)
		with open(newfile, 'w') as f:
			f.write(','.join(self._content))

		return self

if __name__ == '__main__':
    formatTxt = FormatTxt()
    formatTxt.getFilePath('/var/www/py/id.txt').fileOpen().move('/var/www/py/format.txt')
