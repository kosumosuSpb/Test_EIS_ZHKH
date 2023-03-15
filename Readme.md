# Решение тестового задания для ЕИС ЖКХ

## Задача 1

Даны две даты в виде строк формата `YYYY-MM-DD`. Посчитать количество дней между
этими датами без использования библиотек.

#### Примеры:

* Дано: `date1 = "2019-06-29"`, `date2 = "2019-06-30"`
* Результат: `1`

* Дано: `date1 = "2020-01-15"`, `date2 = "2019-12-31"`
* Результат: `15`

### Решено в файле:

`task1.py`

### О решении

Насколько я понял, решать нужно без встроенного модуля `datetime`. Если же его было можно использовать, задача решалась бы существенно проще благодаря `datetime.timedelta`.

Приведено два решения: 

1. методом инкремента от стартовой даты (медленнее)
2. методом рассчёта разницы дней от года стартовой даты (быстрее)

Разница в скорости между двумя решениями довольно приличная:

    >>>d1 = '0001-1-1'
    >>>d2 = '2000-12-12'
    
    >>>t1 = time()
    >>>print(Date.days_diff(d1, d2))
    >>>print(time() - t1)
    730465
    0.001251220703125

    >>>t1 = time()
    >>>print(Date.days_diff_increment(d1, d2))
    >>>print(time() - t1)
    730465
    0.33750367164611816

## Задача 2

Дано целое положительное число "num", представленное в виде строки, и целое
число "k". Вернуть минимальное возможное число, полученное после удаления из
строки k цифр.

#### Примеры:
* Дано: `num = "1432219"`, `k = 3`
* Результат: `"1219"`
* Дано: `num = "10200"`, `k = 1`
* Результат: `"200"`

### Решено в файле:

`task2.py`

## Задача 3

Есть две коллекции (таблицы) данных: accrual (долги) и payment (платежи). Обе
коллекции имеют поля:

- `id`
- `date` (дата)
- `month` (месяц)

Необходимо написать функцию, которая сделает запрос к платежам и найдёт для
каждого платежа долг, который будет им оплачен. Платёж может оплатить только
долг, имеющий более раннюю дату. Один платёж может оплатить только один долг, и
каждый долг может быть оплачен только одним платежом. Платёж приоритетно должен
выбрать долг с совпадающим месяцем (поле `month`). Если такого нет, то самый
старый по дате (поле `date`) долг.

Результатом должна быть таблица найденных соответствий, а также список платежей,
которые не нашли себе долг.

Запрос можно делать к любой базе данных (mongodb, postgresql или другие) любым
способом

### Решено в файлах:

* `./task3/models.py` -- модели для БД
* `./task3/find_accruals.py` -- основное решение
* `./task3/gen_data.py` -- генерация тестовых данных
* `task3_test.py` -- запуск теста (создание БД, генерация данных, поиск решения, выдача результата в консоль)

### О решении:

Использовал PonyORM, т.к. было быстрее всего, плюс, он неплохо читается даже если его читает тот, кто его не знает. 
То же самое, при необходимости можно написать на любом другом ORM, либо на SQL. 

Как БД использовал sqLite, потому что это тоже было проще и быстрее всего (не нужно ставить, например, PostgreSQL)

В поле `month` я хранил тоже дату, т.к. решил, что месяц оплаты/начисления может быть другим, не обязательно прошлым, плюс, так проще им управлять.

В результате я возвращаю два списка: с платежами, для которых не найдено начисление, и с парами платёж - начисление.  