from pony.orm import *
from .models import Accrual, Payment


@db_session
def find_accruals():
    """Находит соответствия Платёж -- Начисление. Если не находит, то берёт самое старое начисление"""
    payments = Payment.select().order_by(Payment.month)[:].to_list()

    lonely_payments = []
    for payment in payments:
        same_month_accrual = Accrual.select(
            lambda a:
            a.month.year == payment.month.year and
            a.month.month == payment.month.month and
            not a.payment
        ).order_by(Accrual.month).first()
        if same_month_accrual:
            payment.accrual = same_month_accrual
        else:
            lonely_payments.append(payment)

    lonely_accruals = Accrual.select(lambda a: not a.payment).order_by(Accrual.month)[:].to_list()
    for payment, accrual in zip(lonely_payments, lonely_accruals):
        payment.accrual = accrual

    lonely_payments = Payment.select(lambda p: not p.accrual)[:].to_list()
    pairs = [(payment, payment.accrual) for payment in Payment.select(lambda p: p.accrual).order_by(Payment.month)[:].to_list()]

    return pairs, lonely_payments
