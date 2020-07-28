from flask import Flask,render_template,request
app = Flask(__name__)
import sqlite3,admin,student


@app.route('/')
def index():
    """首页 显示所有书目"""
    sql = 'select * from book'
    booklist = admin.bookList(sql)
    return render_template('index.html', books = booklist)

@app.route('/Result',methods=['POST'])
def result():
    """查询结果界面"""
    book =[]
    bookname = request.form.get('bookName')
    if bookname == '':
        return '请输入书名'
    else:

        sql = "select * from book where bookname like '%{}%' ".format(bookname)
        book = admin.bookList(sql)
        return render_template('Result.html', bookitem=book)

@app.route('/borrow',methods=['POST'])
def borrow():
    """借阅界面"""
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    bookID = int(request.form.get('bookID'))
    sql = f'select bookname from book where id = {bookID}'
    data = cursor.execute(sql)
    bookname = list(data)[0][0]
    num = int(request.form.get('num'))
    cursor.close()
    conn.close()

    return render_template('borrow.html',booknum = num,bookID = bookID,bookname = bookname)

@app.route('/refer',methods=['POST'])
def refer():
    """借出书籍页面"""
    idStudent = int(request.form.get('idStudent'))
    studentName = request.form.get('studentName')
    num = int(request.form.get('num'))
    bookID = int(request.form.get('bookID'))
    bookName = request.form.get('bookName')

    sign = student.Borrow(idStudent, studentName, bookID, bookName, num)
    if sign:
        text = '借阅成功'
        return render_template('refer.html' ,text = text )
    else:
        text = '库存不足'
        return render_template('refer.html' ,text = text )
@app.route('/return')
def return1():
    '''还书界面'''
    return render_template('return.html')

@app.route('/return2',methods=['POST'])
def return2():
    '''还书成功界面'''
    idStudent = request.form.get('idStudent')
    bookName = request.form.get('bookName')
    student.returnBook(idStudent, bookName)
    return render_template('return2.html')

@app.route('/login')
def login():
    """管理员登录界面"""
    return render_template('login.html')

@app.route('/admin',methods=['POST'])
def adminUI():
    '''管理员界面'''
    actnumber = request.form.get('actnumber')
    password = request.form.get('password')
    if actnumber == 'superUser' and password == '123456':
        sql = 'select * from book'
        booklist = admin.bookList(sql)
        return render_template('admin.html',books = booklist)
    else:
        return index()

@app.route('/delete',methods = ['POST'])
def delete():
    """删除书目"""
    bookID = request.form.get('bookID')
    sql = f'delete from book where id = {bookID}'
    student.Sql(sql)
    booklist = admin.bookList('select * from book')
    return render_template('admin.html',books = booklist)

@app.route('/adminResult',methods=['POST'])
def adResult():

    book = []
    bookname = request.form.get('bookName')
    if bookname == '':
        return '请输入书名'
    else:
        sql = "select * from book where bookname like '%{}%' ".format(bookname)
        book = admin.bookList(sql)
    return render_template('adminResult.html',bookitem = book)

@app.route('/addindex')
def addindex():
    return render_template('addindex.html')

@app.route('/addResult',methods=["POST"])
def addbook():
    bookname = request.form.get('bookName')
    author = request.form.get('author')
    nums = request.form.get('nums')
    admin.addBook(bookname,author,nums)

    return render_template('addResult.html')
if __name__ == '__main__':
    app.run()
