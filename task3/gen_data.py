from datetime import date, timedelta
from pony.orm import *
from random import randint
from typing import List
#
from .models import Accrual, Payment


def date_gen(spread=365) -> date:
    """
    :param spread: разброс по дням
    :return: список дат
    """
    return date.today() - timedelta(days=randint(1, spread))


@db_session
def create_accruals(num=5) -> List[Accrual]:
    return [Accrual(date=(_date := date_gen()), month=(_date - timedelta(days=30))) for _ in range(num)]


@db_session
def create_payments(num=5) -> List[Payment]:
    return [Payment(date=(_date := date_gen()), month=(_date - timedelta(days=randint(1, 366//2)))) for _ in range(num)]


if __name__ == '__main__':
    print('Creating test data in database...')
    create_accruals()
    create_payments()
    print('Test data in database has created')
