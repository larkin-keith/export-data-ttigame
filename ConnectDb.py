#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""webhook for hexo blog"""

__author__ = 'Lavenkin'

import mysql.connector

class ConnectDb(object):

	def __init__(self, host, user, password, db):
		self._host = host
		self._user = user
		self._password = password
		self._db = db

	def connect(self):
		try:
			self._conn = mysql.connector.connect(host = self._host, user = self._user, password = self._password, database = self._db)
			self._cursor = self._conn.cursor()
			# print(self._cursor)
			return self
		except Exception as e:
			print(e)

	def table(self, table):
		self._db_table = table
		return self

	def select(self, select):
		self._db_select = select
		return self

	def whereIn(self, field, data):
		self._db_where_in_field = field
		self._db_where_in_data = data
		return self

	# def select(self, table, fields, conditions):
	# 	""" 简单粗暴处理 """
	# 	# print('select %s from %s where id in (%s)' % (fields, table, conditions))
	# 	self._cursor.execute('select %s from %s where id in (%s)' % (fields, table, conditions))
	# 	return self

	def get(self):
		# print('select %s from %s where id in %s' % (self._db_select, self._db_table, self._db_where))
		self._cursor.execute('select %s from %s where %s in (%s)' % (self._db_select, self._db_table, self._db_where_in_field, self._db_where_in_data))
		return self._cursor.fetchall()

	def close(self):
		self._cursor.close()
		self._conn.close()

if __name__ == '__main__':
    db = ConnectDb('127.0.0.1', 'root', 'root', 'appcenter')
    # print(db.connect().select('softwares_view', 'id,name', '1,2,3').get())
    print(db.connect().table('softwares_view').select('id,name').whereIn('id', '1,2,3').get())
    db.close()