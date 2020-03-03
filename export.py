from pymysql import *
import xlwt
import pandas.io.sql as pds_sql

db_con = connect(
    host="localhost",
    user="root",
    password="password",
    database="pick_email"
)

cursor_connection = db_con.cursor()

df = pds_sql.read_sql('select email,full_name,created_by from email_collection', db_con)

df.to_excel('contacts_mallbd_email.xlsx')

print(df)
