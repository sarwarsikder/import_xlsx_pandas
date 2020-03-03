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

df = pds_sql.read_sql('select *  from email_collection', db_con)

df.to_excel('Assciations_BAIRA_Email.xlsx')

print(df)
