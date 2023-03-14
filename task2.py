"""
    Дано целое положительное число "num", представленное в виде строки, и целое
    число "k". Вернуть минимальное возможное число, полученное после удаления из
    строки k цифр.
    Примеры:
    Дано: num = "1432219", k = 3
    Результат: "1219"
    Дано: num = "10200", k = 1
    Результат: "200"
"""
import unittest


def min_num(num: str, k: int) -> str:
    for _ in range(k):
        num = str(min(int(num[:i] + num[i+1:]) for i in range(len(num))))
    return num


class TestMinNum(unittest.TestCase):
    n1 = "1432219"
    n2 = "10200"
    k1 = 3
    k2 = 1
    expected1 = '1219'
    expected2 = '200'

    def test_case1(self):
        result = min_num(self.n1, self.k1)
        self.assertEqual(self.expected1, result)

    def test_case2(self):
        result = min_num(self.n2, self.k2)
        self.assertEqual(self.expected2, result)


if __name__ == '__main__':
    unittest.main()
