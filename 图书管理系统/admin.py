#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sqlite3
import time

def bookList(sql):
    booklist = []
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    data = cursor.execute(sql)
    for item in data:
        booklist.append(item)
    cursor.close()
    conn.close()
    return booklist

def addBook(bookname,author,nums=0):
    year = time.strftime('%Y')
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    sql = f"select id from book order by id desc limit 0,1"
    ids = cursor.execute(sql)
    num = ''
    try:
        for id in ids:
            num = str(id[0])[4:]
            break
        id = int(year + str(int(num) + 1))
    except:
        id = int(year + '1')
    sql = f'insert into book values ({id},"{bookname}",{nums},"{author}") '
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    year = time.strftime('%Y')
    print(year)

