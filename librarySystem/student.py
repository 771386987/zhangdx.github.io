#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sqlite3
import time
def Sql(sql):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
def Borrow(idStudent,studentName,bookID,bookName,num):
    loantime = time.strftime('%Y-%m-%d')

    if num > 0:
        sql = f'update book set nums = {num - 1} where id = {bookID}'
        Sql(sql)
        time.sleep(3)
        sql = f"insert into student (idStudent,studentName,bookId, bookName,loanDate)values ({idStudent},'{studentName}',{bookID},'{bookName}','{loantime}')"
        Sql(sql)
        return True
    else:
        return False
def returnBook(idStudent,bookName):

    sql = f'update book set nums = nums+1 where bookname = "{bookName}"'
    Sql(sql)
    returntime =  time.strftime('%Y-%m-%d')
    sql = f'update student set returnDate = "{returntime}" where bookName = "{bookName}" and idStudent = {idStudent}'
    Sql(sql)

if __name__ == '__main__':
    time = time.strftime('%Y-%m-%d')
    print(time)