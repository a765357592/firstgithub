import sqlite3
def create_db():
    conn=sqlite3.connect('car.db')
    cur=conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS car(name TEXT)')
    conn.commit()
    conn.close()

def insert_car(name):
    conn=sqlite3.connect('car.db')
    cur=conn.cursor()
    cur.execute('INSERT INTO car VALUES(?,)',(name,))
    conn.commit()
    conn.close()

def view_all():
    conn=sqlite3.connect('car.db')
    cur=conn.cursor()
    cur.execute('SELECT * FROM car')
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows
    

def search_one(name):
    conn=sqlite3.connect('car.db')
    cur=conn.cursor()
    cur.execute('SELECT * FROM car WHERE name=?',(name,))
    one=cur.fetchone()
    conn.commit()
    conn.close()
    return one

def search(name):
    conn=sqlite3.connect('car.db')
    cur=conn.cursor()
    cur.execute('SELECT * FROM car WHERE name LIKE ?',(name+'%',))
    one=cur.fetchone()
    return one
    conn.commit()
    conn.close()

def remove_one(name):
    conn=sqlite3.connect('car.db')
    cur=conn.cursor()
    cur.execute('DELETE FROM car WHERE name=?',(name))
    conn.commit()
    conn.close()

def remove(name):
    conn=sqlite3.connect('car.db')
    cur=conn.cursor()
    cur.execute('DELETE FROM car WHERE name LIKE ?',(name+'%',))
    conn.commit()
    conn.close()

def update_one(name,img,price):
    conn=sqlite3.connect('car.db')
    cur=conn.cursor()
    cur.execute('UPDATE car SET name=?,img=?,price=?',(name,img,price))
    conn.commit()
    conn.close()