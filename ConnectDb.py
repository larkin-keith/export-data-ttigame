#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""webhook for hexo blog"""

__author__ = 'Lavenkin'

import mysql.connector

class ConnectDb(object):

	def __init__(self, host, user, password, db, port):
		self._host = host
		self._user = user
		self._password = password
		self._db = db
		self._port = port

	def connect(self):
		try:
			self._conn = mysql.connector.connect(host = self._host, user = self._user, password = self._password, database = self._db, port = self._port)
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

	def whereIn(self, field, datas):
		self._db_where_in_field = field
		self._db_where_in_datas = datas
		return self

	def where(self, field, condition, data):
		self._db_where_field = field
		self._db_where_condition = condition
		self._db_where_data = data
		return self

	# def select(self, table, fields, conditions):
	# 	""" 简单粗暴处理 """
	# 	# print('select %s from %s where id in (%s)' % (fields, table, conditions))
	# 	self._cursor.execute('select %s from %s where id in (%s)' % (fields, table, conditions))
	# 	return self

	def get(self):
		# print('select %s from %s where %s %s \'%s\' and %s in (%s)' % (
		# 		self._db_select, 
		# 		self._db_table,
		# 		self._db_where_field,
		# 		self._db_where_condition,
		# 		self._db_where_data,
		# 		self._db_where_in_field, 
		# 		self._db_where_in_datas
		# ))
		self._cursor.execute('select %s from %s where %s %s \'%s\' and %s in (%s)' % (
				self._db_select, 
				self._db_table,
				self._db_where_field,
				self._db_where_condition,
				self._db_where_data,
				self._db_where_in_field, 
				self._db_where_in_datas
		))
		return self._cursor.fetchall()

	def close(self):
		self._cursor.close()
		self._conn.close()

if __name__ == '__main__':
    db = ConnectDb('127.0.0.1', 'root', 'root', 'appcenter', '3306')
    # print(db.connect().select('softwares_view', 'id,name', '1,2,3').get())
    print(db.connect().table('softwares_view').select('id,name').where('release_status', '=', 'show').whereIn('id', '1,2,3').get())
    db.close()