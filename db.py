import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cursorObj = self.con.cursor()

    def unfinished_orders(self, date) -> list:
        lst = self.cursorObj.execute("SELECT * FROM orders WHERE status = 0 AND date_of_order = ?",
                                     (date,)).fetchall()
        self.con.commit()
        return list(lst)

    def price_by_id(self, dish_id) -> int:
        lst = self.cursorObj.execute("SELECT dish_price FROM menu WHERE dish_id = ?",
                                     (dish_id,)).fetchall()
        result = lst[0][0]
        self.con.commit()
        return result

    def is_dish_affordable(self, dish_id) -> bool:
        lst = self.cursorObj.execute("SELECT available FROM menu WHERE dish_id = ?", (str(dish_id))).fetchall()
        self.con.commit()
        return bool(lst[0][0])

    def delete_from_cart(self, user_id, dish_id) -> None:
        dishes, total_price = \
            self.cursorObj.execute("SELECT dishes, total_price FROM cart WHERE user_id = ?", (user_id,)).fetchall()[0]

        dishes = dishes[1:-1].split(', ')
        final_dishes = list(map(lambda x: [int(x.split(':')[0]), int(x.split(':')[1])], dishes))
        dish = list(filter(lambda x: x if x[0] == dish_id else None, final_dishes))[0]
        dish[1] -= 1

        if dish[1] <= 0:
            final_dishes = list(filter(lambda x: x if x[0] != dish_id else None, final_dishes))

        total_price = 0

        for [id_, count] in final_dishes:
            total_price += self.price_by_id(id_) * count

        if len(final_dishes) == 0:
            self.cursorObj.execute("DELETE FROM cart WHERE user_id = ?", (dish_id,))
            self.con.commit()

        else:
            final_dishes = list(map(lambda x: f'{str(x[0])}:{str(x[1])}', final_dishes))
            result = f'({", ".join(final_dishes)})'

            self.cursorObj.execute("UPDATE cart SET dishes = ?, total_price = ? WHERE user_id = ?",
                                   (result, total_price, user_id))
            self.con.commit()

    def unfinished_orders_for_user(self, user_id) -> list:
        lst = self.cursorObj.execute("SELECT * FROM orders WHERE status = 0 AND user_id = ?",
                                     (user_id,)).fetchall()
        self.con.commit()
        return list(lst)

    def affordable_dishes(self) -> list:
        lst = self.cursorObj.execute("SELECT dish_id FROM menu WHERE available = 1").fetchall()
        return list(map(lambda x: x[0], lst))

    def delete_dish_from_menu(self, dish_id) -> None:
        self.cursorObj.execute("DELETE FROM menu WHERE dish_id=?", (dish_id,))
        self.con.commit()

    def subtract_balance(self, user_id, amount) -> None:
        self.cursorObj.execute("UPDATE clients SET balance = balance - ? WHERE user_id = ?", (amount, user_id))
        self.con.commit()

    def toggle_dish_availability(self, dish_id) -> None:
        self.cursorObj.execute("UPDATE menu SET available = NOT available WHERE dish_id = ?", (dish_id,))
        self.con.commit()

    def plus_balans(self, user_id, money):
        self.cursorObj.execute('UPDATE clientsSET balance += ? WHERE user_id = ?', (money, user_id))
        self.con.commit()

    def plus_dish_in_bd(self, name, weight, cost):
        self.cursorObj.execute('INSERT INTO menu(dish_name, dish_weight, dish_price, available) '
                               'VALUES(?, ?, ?, 0)', (name, weight, cost))
        self.con.commit()

    def cart_to_order(self, user_id):
        self.cursorObj.execute('''INSERT 
                              INTO orders(dishes, total_price) 
                              VALUES(SELECT dishes, total_price 
                                    FROM cart 
                                    WHERE user_id = ?)
                              WHERE user_id = ?
                                                              ''', (user_id,))
        cursor2 = self.con.cursor()
        cursor2.execute('''DELETE 
                          FROM cart
                          WHERE user_id = ?
                                                          ''', (user_id,))
        self.con.commit()

    def info_cart(self, user_id):
        self.cursorObj.execute('''SELECT dishes, total price
                          FROM cart
                          WHERE user_id = ?
                                              ''', (user_id,))
        return self.cursorObj.fetchall()

    def all_order_for_client(self, user_id):
        self.cursorObj.execute('''SELECT
                              FROM orders
                              WHERE user_id = ?
                                                  ''', (user_id,))
        return self.cursorObj.fetchall()

    def all_order_not_for_client(self):
        conn = sqlite3.connect('yfpd')
        cursor = conn.cursor()
        cursor.execute('SELECT FROM orders')
        return self.cursorObj.fetchall()

    def plus_from_cart(self, user_id, dish_id) -> None:
        dishes, total_price = \
            self.cursorObj.execute("SELECT dishes, total_price FROM cart WHERE user_id = ?", (user_id,)).fetchall()[0]

        dishes = dishes[1:-1].split(', ')
        final_dishes = list(map(lambda x: [int(x.split(':')[0]), int(x.split(':')[1])], dishes))
        dish = list(filter(lambda x: x if x[0] == dish_id else None, final_dishes))[0]
        dish[1] += 1

        total_price = 0

        for [id_, count] in final_dishes:
            total_price += self.price_by_id(id_) * count


db = Database('database.db')
