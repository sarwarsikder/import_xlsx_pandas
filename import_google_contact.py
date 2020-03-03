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
        sql = "SELECT phone_number FROM phone_collection WHERE phone_number LIKE '{}' LIMIT 1".format(
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


def insert_phone_number(phone_number, date, create_by):
    try:
        sql = """INSERT INTO phone_collection (phone_number, created_by) VALUES ("{}","{}");""".format(
            phone_number, create_by)
        # print(sql)
        cursor_connection.execute(sql)
        db_con.commit()
    except Exception as e:
        print('s0 insertion', str(e))


if __name__ == '__main__':
    # pd__data_obj = pds.read_excel('ovi.xlsx')
    pd__data_obj = pds.read_excel('tanveer.xlsx',
                                  converters={'Mobile': str})
    pd_data_value = pds.DataFrame(pd__data_obj, columns=['Mobile']).dropna()

    for target_item in pd_data_value.index:

        phone_number = str(pd_data_value['Mobile'][target_item]).strip()

        ##print("fddfdfdf" + phone_number)
        print(str(phone_number))

        if str(phone_number) == 'nan':
            print(type(phone_number))

        if phone_number != "" or phone_number != 'nan':
            # print(type(phone_number))
            # print(phone_number)

            created_by = "Ashraf Tanveer"

            if ":::" in phone_number:
                seg_phones = phone_number.split(":::")
                for item in seg_phones:
                    print("Double Number" + item)
                    if find_existing_phone_number(item) == False:
                        insert_phone_number(item, str('25-02-2020'), created_by)
                        # print("New ONe")
            else:

                if find_existing_phone_number(phone_number) == False:
                    # print("Single Number " + phone_number)
                    insert_phone_number(phone_number, str('25-02-2020'), created_by)
                    # print("New ONe")

            # print(phone_number.find(":::"))
