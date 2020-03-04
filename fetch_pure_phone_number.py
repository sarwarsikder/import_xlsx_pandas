import pandas as pds

from entities import pure_phone_collection
from entities.pure_phone_collection import PurePhoneCollection

if __name__ == '__main__':
    file_name = 'xlsx/Assciations.xlsx';
    sheet_names = [
        {
            "key": "BGAPMEA",
            "phone": ["Phone Number"],
            "name": "Company Name",
            "email": "Email",
            "address": "Address",
        }
        ,
        {
            "key": "AHCAB",
            "phone": ["Phone"],
            "name": "Name",
            "email": "Email",
            "address": "Address",
        }
        ,
        {
            "key": "BACE",
            "phone": ["Phone"],
            "name": "Contact Person",
            "email": "Email",
            "address": "Address",
        }
        ,
        {
            "key": "ECAB",
            "phone": ["Phone"],
            "name": None,
            "email": "Email",
            "address": "Address",
        }
        ,
        {
            "key": "BAB",
            "phone": ["Contact"],
            "name": None,
            "email": "Email",
            "address": "Address",
        }
        ,
        {
            "key": "BAMA",
            "phone": ["Phone"],
            "name": "Company Name",
            "email": "Email",
            "address": "Address",
        }
        ,
        {
            "key": "BASIS",
            "phone": ["Phone", "Contact Number"],
            "name": "Company Name",
            "email": "Email",
            "address": "Address",
        }
        ,
        {
            "key": "ATAB",
            "phone": ["Phone"],
            "name": "Name",
            "email": "Email",
            "address": "Address",
        }
        ,
        {
            "key": "BAIRA",
            "phone": ["Phone", "Mobile"],
            "name": "Company Name",
            "email": "Email",
            "address": "Address",
        }
        ,
        {
            "key": "BACI",
            "phone": ["Phone"],
            "name": "Name",
            "email": "Email",
            "address": "Address",
        }
        ,
        {
            "key": "BARVIDA",
            "phone": ["Phone"],
            "name": "Company Name",
            "email": "Email",
            "address": "Address",
        }
        ,
        {
            "key": "ABMEAB",
            "phone": ["Phone"],
            "name": "Company Name",
            "email": "Email",
            "address": "Address",
        }
    ]

    counter = 0;
    for sheet_name in sheet_names:
        print("--------------------" + sheet_name['key'] + "-----------------------")
        pd__data_obj = pds.read_excel(file_name, sheet_name['key'])
        pd_data_value = pds.DataFrame(pd__data_obj)
        for target_item in pd_data_value.index:
            for val in sheet_name['phone']:
                try:
                    for pn in pure_phone_collection.phone_number(str(pd_data_value[val][target_item]).strip().lower()):
                        pc = PurePhoneCollection(None, None, None, None, None)
                        pc.phone_number = pn
                        if sheet_name['email'] != None:
                            pc.email = str(pd_data_value[sheet_name['email']][target_item]).strip()
                            if (pc.email == "nan"):
                                pc.email = ""
                        if sheet_name['address'] != None:
                            pc.address = str(pd_data_value[sheet_name['address']][target_item]).strip()
                            if (pc.address == "nan"):
                                pc.address = ""
                        if sheet_name['name'] != None:
                            pc.full_name = str(pd_data_value[sheet_name['name']][target_item]).strip()
                            if (pc.full_name == "nan"):
                                pc.full_name = ""
                        pc.created_by = sheet_name['key']
                        pc.save()
                        counter = counter + 1
                        if counter % 100 == 0:
                            print("Saved :" + str(counter))
                except Exception as e:
                    print('Error', str(e))
