import mysql.connector
import pandas as pds
import datetime as date_time
import re

db_con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="pick_email"
)

cursor_connection = db_con.cursor()
sql_transaction = []


# Define a function for
# for validating an Email
def email_checker(email):
    # pass the regualar expression
    # and the string in search() method
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if (re.search(regex, email)):
        return True

    else:
        return False


def transaction_bldr(sql):
    global sql_transaction
    sql_transaction.append(sql)
    # print(sql)
    if len(sql_transaction) > 100:
        db_con.execute('BEGIN TRANSACTION')
        for s in sql_transaction:
            try:
                db_con.execute(s)
            except:
                pass
        cursor_connection.commit()
        sql_transaction = []


def find_existing_phone_number(email):
    try:
        sql = "SELECT email FROM email_collection WHERE email LIKE '{}' LIMIT 1".format(
            '%' + email + '%')
        # print(sql)
        cursor_connection.execute(sql)
        result = cursor_connection.fetchone()
        if result != None:
            return result[0]
        else:
            return False
    except Exception as e:
        print(str(e))
        return False


def insert_email_number(email, date, create_by):
    try:
        if email_checker(email):
            sql = """INSERT INTO email_collection ( email , created_by) VALUES ("{}","{}");""".format(
                email, create_by)
            # print(sql)
            cursor_connection.execute(sql)
            db_con.commit()
    except Exception as e:
        print('s0 insertion', str(e))


if __name__ == '__main__':
    # pd__data_obj = pds.read_excel('ovi.xlsx')
    pd__data_obj = pds.read_excel('Assciations.xlsx',
                                  sheet_name='BAIRA',
                                  converters={'Email': str})
    pd_data_value = pds.DataFrame(pd__data_obj, columns=['Email']).dropna()

    for target_item in pd_data_value.index:

        email = str(pd_data_value['Email'][target_item]).strip()

        created_by = "Assciations--BAIRA"

        if "," in email:
            seg_phones = email.split(",")
            for item in seg_phones:
                print(item)
                print("------>>>>>>>>-------")
                insert_email_number(item, str('25-02-2020'), created_by)
                # if find_existing_phone_number(item):
                #     print(item)
                #     insert_email_number(item, str('25-02-2020'), created_by)
        elif ";" in email:
            seg_phones = email.split(";")
            for item in seg_phones:
                print(item)
                print("------>>>>>>>>-------")
                insert_email_number(item, str('25-02-2020'), created_by)
                # if find_existing_phone_number(item):
                #     print(item)
                #     insert_email_number(item, str('25-02-2020'), created_by)
        elif ";" in email:
            seg_phones = email.split(" ")
            for item in seg_phones:
                print(item)
                print("------>>>>>>>>-------")
                insert_email_number(item, str('25-02-2020'), created_by)
                # if find_existing_phone_number(item):
                #     print(item)
                #     insert_email_number(item, str('25-02-2020'), created_by)
        else:
            print(email)
            insert_email_number(email, str('25-02-2020'), created_by)
            # if find_existing_phone_number(email):
            #     print(email)
            #     insert_email_number(email, str('25-02-2020'), created_by)
