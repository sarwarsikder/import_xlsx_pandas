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
    pd__data_obj = pds.read_excel('Assciations.xlsx',
                                  sheet_name='BGAPMEA',
                                  converters={'Phone Number': str})
    pd_data_value = pds.DataFrame(pd__data_obj, columns=['Phone Number']).dropna()

    for target_item in pd_data_value.index:

        phone_number = str(pd_data_value['Phone Number'][target_item]).strip()

        ##print("fddfdfdf" + phone_number)

        if str(phone_number) == 'nan':
            print(type(phone_number))

        if len(phone_number) >= 9:
            # print(type(phone_number))
            # print(phone_number)

            # print(str("Phone--------F " + phone_number))

            if "," in phone_number:
                seg_phones = phone_number.split(",")
                for item in seg_phones:
                    if len(
                            item) > 9 and 'Fax:' not in item and 'Pho:' not in item and 'Fax :' not in item and '-02-' not in item and '-2-' not in item and '02' not in item:
                        # print(seg_phones)
                        if len(item.lstrip('Mobile: ').lstrip('Cell :').lstrip('Tel: ')) >= 9:


                            temp_number = item.lstrip('Mobile: ').lstrip('Cell :').lstrip('Tel: ')

                            if 'Cell :' in item:
                                temp_number.split('Cell :')
                                if len(temp_number[1]) > 9:
                                 print(temp_number[1].replace(' ', '').replace('-', ''))
                            else:
                                print(item.lstrip('Mobile: ').lstrip('Cell :').lstrip('Tel: ').replace(' ', '').replace('-', '').replace('/', ''))

                    # print("New ONe")

            created_by = "Assciations--BGAPMEA"

            # if ":::" in phone_number:
            #     seg_phones = phone_number.split(":::")
            #     for item in seg_phones:
            #         print("Double Number" + item)
            #         if find_existing_phone_number(item) == False:
            #             insert_phone_number(item, str('25-02-2020'), created_by)
            #             # print("New ONe")
            # else:
            #
            #     if find_existing_phone_number(phone_number) == False:
            #         # print("Single Number " + phone_number)
            #         insert_phone_number(phone_number, str('25-02-2020'), created_by)
            #         # print("New ONe")

            # print(phone_number.find(":::"))
