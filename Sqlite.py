#!/usr/bin/python


#后续务必要更改db文件存在位置


import sqlite3


def create_table():
	
	#只创建一次表

	conn = sqlite3.connect('D:/data.db')
	print("Opened database successfully")
	c = conn.cursor()
	c.execute('''CREATE TABLE KEYDATA
       (NAME TEXT ,
       DUE    TEXT);''')

	c.execute('''CREATE TABLE USERDATA
       (NAME TEXT ,
       DUE            TEXT ,
       KEY        TEXT,
       DEADLINE     TEXT,
       BZX         TEXT);''')
	print("Two tables created successfully")
	conn.commit()
	conn.close()



def insert_element_in_KEYDATA(name,due):
	
	#向KEYDATA传入四项参数，不要有漏

	conn = sqlite3.connect('D:/data.db')
	print("Opened database successfully")
	c = conn.cursor()

	c.execute("INSERT INTO KEYDATA (NAME,DUE) \
	      VALUES (%r,%r)" %(name,due) ) 
	print("successful")

	conn.commit()
	conn.close()



def insert_element_in_USERDATA(name,due,key,deadline,bzx):
	
	#向USERDATA传入四项参数，不要有漏

	conn = sqlite3.connect('D:/data.db')
	print("Opened database successfully")
	c = conn.cursor()

	c.execute("INSERT INTO USERDATA (NAME,DUE,KEY,DEADLINE,BZX) \
	      VALUES (%r,%r,%r,%r,%r)" %(name,due,key,deadline,bzx) ) 
	print("successful")

	conn.commit()
	conn.close()






def return_value_except_first(name):
	try:
		#提取USERDATA除了第一个值后面的所有值
		conn = sqlite3.connect('D:/data.db')
		c = conn.cursor()
		print("Opened database successfully")

		c.execute("SELECT DUE, KEY, DEADLINE, BZX FROM USERDATA WHERE NAME=(%r)" %(name))
		a = c.fetchall();

		conn.commit()
		conn.close()
		a = a[0]
		due = a[0]
		key = a[1]
		deadline = a[2]
		bzx = a[3]

		return due, key, deadline, bzx
	except:
		error = '0', '0', '0', '0'
		return error


def test(b):
	if b == '707':
		print('F')
		return '0', '0', '0', '0'
