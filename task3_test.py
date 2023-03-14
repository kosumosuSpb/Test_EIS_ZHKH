from pony.orm import db_session
from task3.models import Accrual, Payment
from task3.gen_data import create_accruals, create_payments
from task3.find_accruals import find_accruals

if __name__ == '__main__':
    print('Create entities in DB...')
    create_accruals()
    create_payments()
    print('Ok')

    with db_session:
        accruals = Accrual.select().order_by(Accrual.date)[:].to_list()
        payments = Payment.select().order_by(Payment.month)[:].to_list()
        print('Accruals:', [accrual.month for accrual in accruals])
        print('Payments:', [payment.month for payment in payments])

    print('Find pairs...')
    pairs, not_found = find_accruals()
    print('Pairs in DB:', [(p.month, a.month) for p, a in pairs])
    print('Not found payments:', [(p.month, a.month) for p, a in not_found])
    print('Complete')
