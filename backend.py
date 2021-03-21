import sqlite3

def connection():
  conn=sqlite3.connect('library.db')
  conn.execute('CREATE TABLE if not exists library (id integer PRIMARY KEY AUTOINCREMENT, title text not null, author text not null, year integer, isbn text)')
  conn.commit()
  conn.close()

def insert(title,author,year,isbn):
  conn=sqlite3.connect('library.db')
  conn.execute("INSERT INTO library VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
  conn.commit()
  conn.close()

def view():
  conn=sqlite3.connect('library.db')
  cur_obj=conn.cursor()
  cur_obj.execute("SELECT * from library")
  rows=cur_obj.fetchall()
  conn.close()
  return rows

def update(id,title,author,year,isbn):
  conn=sqlite3.connect('library.db')
  conn.execute("UPDATE library SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
  conn.commit()
  conn.close()

def delete(id):
  conn=sqlite3.connect('library.db')
  conn.execute("DELETE from library WHERE id=?",(id,))
  conn.commit()
  conn.close()

def search(title='',author='',year='',isbn=''):
  conn=sqlite3.connect('library.db')
  cur_obj=conn.cursor()
  cur_obj.execute("SELECT * from library WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
  rows=cur_obj.fetchall()
  conn.close()
  return rows

connection()