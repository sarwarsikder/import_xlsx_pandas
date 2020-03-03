from pymysql import connect

db_con = connect(
    host="192.168.1.51",
    user="root",
    password="password",
    database="pick_email"
)


def save(sql):
    try:
        db_con.cursor().execute(sql)
        db_con.commit()
    except Exception as e:
        print('Error', str(e))
