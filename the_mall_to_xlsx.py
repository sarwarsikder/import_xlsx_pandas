from pymysql import *
import xlwt
import pandas.io.sql as pds_sql

db_con = connect(
    host="localhost",
    user="root",
    password="password",
    database="the_mall_bd"
)

cursor_connection = db_con.cursor()

df = pds_sql.read_sql('select id,firstname,lastname,email,primary_phone,secondary_phone  from users', db_con)

df.to_excel('mallbd_contacts.xlsx')

print(df)
