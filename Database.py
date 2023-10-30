# database.py

from tabulate import tabulate
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="root", database="python_db")

def insert(name, age, city):
    res = con.cursor()
    sql = "insert into users (name,age,city) values (%s,%s,%s)"
    user = (name, age, city)
    res.execute(sql, user)
    con.commit()

def update(name, age, city, id):
    res = con.cursor()
    sql = "update users set name=%s,age=%s,city=%s where id=%s"
    user = (name, age, city, id)
    res.execute(sql, user)
    con.commit()

def select():
    res = con.cursor()
    sql = "SELECT ID,NAME,AGE,CITY from users"
    res.execute(sql)
    result = res.fetchall()
    return result

def delete(id):
    res = con.cursor()
    sql = "delete from users where id=%s"
    user = (id,)
    res.execute(sql, user)
    con.commit()
def create_table(table_name, columns):
    cursor = con.cursor()
    column_definitions = ', '.join(columns)
    cursor.execute(f"CREATE TABLE {table_name} ({column_definitions})")
    con.commit()
