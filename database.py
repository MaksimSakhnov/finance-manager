import sqlite3


def connect_database():
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS balance(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        current_balance INTEGER)""")

        num = cursor.execute("""SELECT COUNT(*) FROM balance""").fetchone()[0]

        if (num == 0):
            cursor.execute("""INSERT INTO balance(current_balance) VALUES (0)""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS operations(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    op_type STRING,
                    sum INTEGER,
                    type STRING,
                    date STRING
        )""")
        cursor.close()


def add_operation(type, t_sum, t_type, t_date):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        if (type == 1):
            type = "Доход"
        elif (type == 2):
            type = "Расход"

        cursor.execute("""INSERT INTO operations(op_type, sum, type, date) VALUES (?, ?, ?, ?)""",
                       (type, t_sum, t_type, t_date))

        # если у нас расход, соответсвенно сумма будет отрицательной
        t_sum = int(t_sum)
        if (type == "Расход"):
            t_sum *= (-1)

        # получаем текущий баланс из таблицы
        cur_balance = cursor.execute("SELECT current_balance FROM balance WHERE id = 1").fetchone()[0]
        cur_balance = int(cur_balance)

        # складываем баланс из бд с вводимой суммой
        cur_balance += t_sum
        cur_balance = str(cur_balance)

        # обновляем баланс в бд
        cursor.execute('UPDATE balance SET current_balance=? WHERE id = 1', (cur_balance,))

        # подверждаем изменения
        db.commit()
        cursor.close()


def get_last_operations():
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()

        # считаем количество записей в таблице с операциями
        response = cursor.execute("""SELECT COUNT(*) FROM operations""")
        num = response.fetchone()[0]

        # если записей меньше 20, выводим все, если больше выводим последние 20
        if (num <= 20):
            response = cursor.execute("SELECT * FROM operations").fetchall()
            return response
        else:
            response = cursor.execute("""SELECT * FROM operations ORDER BY id LIMIT 20""").fetchall()
            return response


def get_data_for_grafic():
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        response = cursor.execute("""SELECT * FROM operations WHERE op_type='Расход' ORDER BY id """).fetchall()
        return response


def get_all_operations(filter):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        if (len(filter) == 0):
            # получаем все записи из таблицы операций в обратном порядке
            response = cursor.execute("""SELECT * FROM operations ORDER BY id """).fetchall()
            return response
        else:
            if (filter[1] == filter[2] and filter[0] == ''):
                response = cursor.execute("""SELECT * FROM operations ORDER BY id """).fetchall()
                return response
            # фильтрация по типу
            elif (filter[1] == filter[2] and filter[0] != ''):
                response = cursor.execute("""SELECT * FROM operations WHERE op_type=(?) ORDER BY id """,
                                          (filter[0],)).fetchall()
                return response
            # по дате
            elif (filter[1] != filter[2] and filter[0] == ''):

                response = cursor.execute("""SELECT * FROM operations WHERE date BETWEEN (?) AND (?) ORDER BY id """,
                                          (filter[1], filter[2])).fetchall()

                return response
            # по типу и дате
            elif (filter[1] != filter[2] and filter[0] != ''):
                response = cursor.execute(
                    """SELECT * FROM operations WHERE date >= (?) AND date <=(?) AND op_type=(?) ORDER BY id """,
                    (filter[1], filter[2], filter[0])).fetchall()
                return response
            else:
                response = cursor.execute("""SELECT * FROM operations ORDER BY id """).fetchall()
                return response


def get_balance():
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        # получаем значение баланса из таблицы баланс
        response = cursor.execute("""SELECT current_balance FROM balance WHERE id=1""").fetchone()[0]
        return (response)
