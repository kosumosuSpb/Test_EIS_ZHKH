"""
Задача 1.

Даны две даты в виде строк формата YYYY-MM-DD. Посчитать количество дней между
этими датами без использования библиотек.

Примеры:

Дано: date1 = "2019-06-29", date2 = "2019-06-30"
Результат: 1

Дано: date1 = "2020-01-15", date2 = "2019-12-31"
Результат: 15
"""
import unittest


class Date:
    def __init__(self, date_string: str):
        assert isinstance(date_string, str), 'Argument must be str!'
        self.year, self.month, self.day = map(int, date_string.split('-'))
        self.is_valid(self.day, self.month, self.year)

    _DAYS_COUNT = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
        }

    @staticmethod
    def is_leap(year: int) -> bool:
        """Возвращает True, если год високосный, False -- если не високосный"""
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @classmethod
    def days(cls, month: int, year: int) -> int:
        """Возвращает количество дней в месяце month в году year"""
        return 29 if cls.is_leap(year) and month == 2 else cls._DAYS_COUNT[month]

    @classmethod
    def is_valid(cls, day, month, year):
        """Проверяет валидность введённой даты"""
        assert 9999 >= year > 0, 'Year must be in range 0 - 9999!'
        assert 0 < month < 13, 'Month must be in range 1 - 12!'
        days = cls.days(month, year)
        assert 0 < day <= days, f'Day must be in range 1 - {days} or 1 - 31/30 in other months'

    @classmethod
    def days_diff_increment(cls, date1: str, date2: str) -> int:
        """Возвращает количество дней в int между введёнными датами (даты в формате YYYY-MM-DD) методом инкремента"""
        date1 = cls(date1)
        date2 = cls(date2)

        if date1 > date2:
            start_date, finish_date = date2, date1
        elif date2 > date1:
            start_date, finish_date = date1, date2
        else:
            return 0

        _day_counter = 0
        while start_date < finish_date:
            start_date._day_increment()
            _day_counter += 1

        return _day_counter

    @classmethod
    def days_diff(cls, date1: str, date2: str) -> int:
        """
        Возвращает количество дней в int между введёнными датами (даты в формате YYYY-MM-DD)
        методом подсчёта разницы количества дней от самой ранней даты
        """
        date1 = cls(date1)
        date2 = cls(date2)

        if date1 > date2:
            start_date, finish_date = date2, date1
        elif date2 > date1:
            start_date, finish_date = date1, date2
        else:
            return 0

        # ищем количество дней между годами
        days_years = 0
        for year in range(start_date.year, finish_date.year):
            days_years += 366 if cls.is_leap(year) else 365

        # сколько прошло дней от начала года до стартовой даты
        start_year_days = cls._days_from_year_start(start_date)

        # сколько дней прошло от начала года в финишной дате до дня финишной даты
        finish_year_days = cls._days_from_year_start(finish_date)

        # считаем разницу между днями
        return finish_year_days + days_years - start_year_days

    @classmethod
    def _days_from_year_start(cls, date) -> int:
        """Возвращает количество дней с начала года"""
        days = 0
        for month in range(1, date.month):
            days += 29 if cls.is_leap(date.year) and month == 2 else cls._DAYS_COUNT[month]
        days += date.day

        return days

    def _day_increment(self):
        if self.day < self.days(self.month, self.year):
            self.day += 1
        else:
            self._month_increment()
            self.day = 1

    def _month_increment(self):
        if self.month < 12:
            self.month += 1
        else:
            self._year_increment()
            self.month = 1

    def _year_increment(self):
        self.year += 1

    def __eq__(self, other):
        """Определяет поведение оператора равенства, =="""
        return self.day == other.day and self.month == other.month and self.year == other.year

    def __ne__(self, other):
        """Определяет поведение оператора неравенства, !="""
        return self.day != other.day or self.month != other.month or self.year != other.year

    def __lt__(self, other):
        """Определяет поведение оператора меньше, <"""
        return self.year < other.year or \
               (self.year == other.year and self.month < other.month) or \
               (self.year == other.year and self.month == other.month and self.day < other.day)

    def __gt__(self, other):
        """Определяет поведение оператора больше, >"""
        return self.year > other.year or \
               (self.year == other.year and self.month > other.month) or \
               (self.year == other.year and self.month == other.month and self.day > other.day)

    def __repr__(self):
        return f'Date[{self.year}-{self.month}-{self.day}]'


class TestDate(unittest.TestCase):
    d1 = "2019-06-29"
    d2 = "2019-06-30"
    d3 = "2020-01-15"
    d4 = "2019-12-31"
    expected1 = 1
    expected2 = 15

    def test_date1_increment_method(self):
        result = Date.days_diff_increment(self.d1, self.d2)
        self.assertEqual(self.expected1, result)

    def test_date2_increment_method(self):
        result = Date.days_diff_increment(self.d3, self.d4)
        self.assertEqual(self.expected2, result)

    def test_date1_reference_year_method(self):
        result = Date.days_diff(self.d1, self.d2)
        self.assertEqual(self.expected1, result)

    def test_date2_reference_year_method(self):
        result = Date.days_diff(self.d3, self.d4)
        self.assertEqual(self.expected2, result)


if __name__ == '__main__':
    unittest.main()
