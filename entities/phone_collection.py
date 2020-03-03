import re


class PhoneCollection:
    def __init__(self, phone_number, address, full_name, email, created_by):
        self.phone_number = phone_number
        self.address = address
        self.full_name = full_name
        self.email = email
        self.created_by = created_by

    def save(self):
        sql = """INSERT INTO phone_collection(phone_number, address, full_name, email, created_at, created_by ) VALUES ("{}","{}","{}","{}", now(),"{}");""".format(
            self.phone_number, self.address, self.full_name, self.email, self.created_by)
        from entities import db_conn
        db_conn.save(sql)


def phone_number(ph):
    ret_val = []
    if ph != "nan":
        data = re.findall(r"([0-9]{3}\s[0-9]{4})|([0-9]{3,6}\s[0-9]{1,9})|([0-9\+\-]{4,30})", ph)
        if len(data) > 0:
            for t2 in data:
                for t in t2:
                    t = t.replace("-", "")
                    t = t.replace("+", "")
                    t = t.replace(" ", "")
                    if len(t.strip()) > 3:
                        ret_val.append(t)
    return ret_val
