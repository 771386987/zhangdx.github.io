#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sqlite3
book = []
conn = sqlite3.connect('library.db')
cursor = conn.cursor()
idStudent = 171341218
name = '张浩泽'
bookID = 202001
bookName = '斗罗大陆'
# sql = '''insert into student values (%d,"张浩泽",21,%s)'''%(idStudent,bookName)
# sql = "insert into student values ({},'{}',{},'{}')".format(idStudent,name,bookID,bookName)
# sql = f"update book set nums = nums+1 where bookname = '{bookName}'"
# sql = f'update student set returnDate = "2020-7-27" where bookName = "斗罗大陆2"'
sql = "select * from student"
id = cursor.execute(sql)
print(id)
conn.commit()
cursor.close()
conn.close()
