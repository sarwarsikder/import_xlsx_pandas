import mysql.connector
import pandas as pds
import datetime as date_time

db_con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="pick_email"
)

cursor_connection = db_con.cursor()
sql_transaction = []


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


def find_existing_phone_number(phone_number):
    try:
        sql = "SELECT email FROM email_collection WHERE email LIKE '{}' LIMIT 1".format(
            '%' + phone_number + '%')
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


def insert_phone_number(phone_number, full_name, email, created_by):
    try:
        sql = """INSERT INTO email_collection (phone_number,full_name, email,created_by) VALUES ("{}","{}","{}","{}");""".format(
            phone_number, full_name, email, created_by)
        # print(sql)
        cursor_connection.execute(sql)
        db_con.commit()
    except Exception as e:
        print('s0 insertion', str(e))


if __name__ == '__main__':
    # pd__data_obj = pds.read_excel('ovi.xlsx')
    pd__data_obj = pds.read_excel('mallbd_contacts.xlsx',
                                  converters={'firstname': str, 'lastname': str, 'email': str, 'primary_phone': str,
                                              'secondary_phone': str})
    pd_data_value = pds.DataFrame(pd__data_obj, columns=['firstname', 'lastname', 'email', 'primary_phone',
                                                         'secondary_phone']).dropna()

    for target_item in pd_data_value.index:

        phone_number = "88" + str(pd_data_value['primary_phone'][target_item]).strip()
        email = str(pd_data_value['email'][target_item]).strip()
        full_name = str(pd_data_value['firstname'][target_item]).strip() + " " + str(
            pd_data_value['lastname'][target_item]).strip()

        ##print("fddfdfdf" + phone_number)
        print(str(phone_number) + "--" + email)
        print(str(full_name) + "--" + email)

        if str(phone_number) == 'nan':
            print(type(phone_number))

        if phone_number != "" or phone_number != 'nan':
            # print(type(phone_number))
            # print(phone_number)

            created_by = "The Mall BD"

            if ":::" in phone_number:
                seg_phones = phone_number.split(":::")
                for item in seg_phones:
                    print("Double Number" + item)
                    if find_existing_phone_number(email) == False:
                        insert_phone_number(item, full_name, email, created_by)
                        # print("New ONe")
            else:

                if find_existing_phone_number(email) == False:
                    # print("Single Number " + phone_number)
                    insert_phone_number(phone_number, full_name, email, created_by)
                    # print("New ONe")

            # print(phone_number.find(":::"))
