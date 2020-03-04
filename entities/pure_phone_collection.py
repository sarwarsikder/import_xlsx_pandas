import re


class PurePhoneCollection:
    def __init__(self, phone_number, address, full_name, email, created_by):
        self.phone_number = phone_number
        self.address = address
        self.full_name = full_name
        self.email = email
        self.created_by = created_by

    def save(self):
        sql = """INSERT INTO pure_phone_collection(phone_number, address, full_name, email, created_at, created_by ) VALUES ("{}","{}","{}","{}", now(),"{}") ON DUPLICATE KEY UPDATE created_at=now();""".format(
            self.phone_number, self.address, self.full_name, self.email, self.created_by)
        from entities import db_conn
        db_conn.save(sql)


def phone_number(ph):
    ret_val = []
    if ph != "nan":
        ph = ph.replace("-", "")
        ph = ph.replace("+", "")
        ph = ph.replace(" ", "")
        data = re.findall(r"1+[3-9]+[0-9]{8}", ph)
        if len(data) > 0:
            for t in data:
                t = "+880" + t
                if len(t) == 14:
                    ret_val.append(t)
    return ret_val
