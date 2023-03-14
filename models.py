import datetime
from pony.orm import *


db = Database()
db.bind(provider='sqlite', filename='db.sqlite', create_db=True)


class Accrual(db.Entity):
    id = PrimaryKey(int, auto=True)
    date = Required(datetime.date)
    month = Required(datetime.date)
    payment = Optional('Payment')


class Payment(db.Entity):
    id = PrimaryKey(int, auto=True)
    date = Required(datetime.date)
    month = Required(datetime.date)
    accrual = Optional(Accrual)


db.generate_mapping(create_tables=True)
