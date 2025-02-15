from __future__ import annotations
from json import load, dump, JSONDecodeError


class MenuAndAdd:
    def __init__(self, identification):
        self.identification = identification
        self.menu = {
            "Гавайская": [100, 150, ["сырный соус", "ветчина", "филе цыпленка", "ананасы", "сыр моцарелла", "базилик"]],
            "Грибная": [100, 150, ["чесночный соус", "ветчина", "свежие шампиньоны", "сыр моцарелла", "базилик"]],
            "Пепперони": [100, 150, ["пицца - соус", "пепперони", "сыр моцарелла", "базилик"]],
            "Сырный цыпленок": [100, 150,
                                ["сырный соус", "филе цыпленка", "свежие томаты", "сыр моцарелла", "базилик"]],
            "Тунец - тысяча островов": [200, 300, ["соус тысяча островов", "тунец", "маслины", "сыр моцарелла", "лимон",
                                                   "базилик"]]}

        self.ingred_order = {"сырный-соус": 50,
                             "чесночный-соус": 50,
                             "пицца-соус": 50,
                             "соус-тысяча-островов": 50,
                             "ветчина": 50,
                             "филе-цыпленка": 50,
                             "ананас": 50,
                             "пепперони": 50,
                             "сыр-моцарелла": 50,
                             "тунец": 50,
                             "маслины": 50,
                             "базилик": 50,
                             "свежие-томаты": 50,
                             "свежие-шампиньоны": 50, }

    def get_ingred(self):
        ingred_list = []
        for i in self.ingred_order.keys():
            ingred_list.append(i)
        return ingred_list

    def admin_or_user(self):
        if self.identification == 'Admin':
            change_menu = input('Желаете ли изменить меню')
            if change_menu == 'да':
                choice = input('Выберите желаемое действие\n1.Удалить позицию\n2.Добавить позицию\n')
                if choice == '1':
                    del_position = input('Что желаете убрать?')
                    try:
                        del self.menu[del_position]

                    except KeyError:
                        print('Нет такой пиццы')

                elif choice == '2':
                    pizza_list_admin = []
                    ingred_list = []
                    name = input('Введите название пиццы')
                    weight = int(input('Введите вес пиццы'))
                    price = int(input('Введите стоймость пиццы'))
                    ingredient = input("Введите состав пиццы")
                    ingred_list.append(ingredient)
                    pizza_list_admin.append(weight)
                    pizza_list_admin.append(price)
                    pizza_list_admin.append(ingred_list)
                    self.menu[name] = pizza_list_admin

        elif self.identification == 'User':
            return self.menu
        return self.menu

    def get_menu(self):
        menu_list = []
        for i in self.menu.keys():
            menu_list.append(i)
        return menu_list

    def user_choise(self):
        user_choice = input(f"Выберите пиццу\nEсли хотите собрать свою, напишите Своя пицца:{self.get_menu()}")
        if user_choice == "Своя пицца":

            user_ingred = input(
                f"Выберите ингредиенты для своей пиццы:\n{self.get_ingred()}\nИнгредиенты вводить через пробел и ингредиенты из двух слов вводить через тире")
            pizza_user = PizzaUser(user_ingred, self.ingred_order)
            pizza_user.get_user_pizza()
            json_work = WorkWithJson(pizza_user.pizza_user_json_key(), pizza_user.pizza_user_json_value())
            json_work.create_json()

        else:
            add_ingred_choice = input(
                "Выберите добавки, если не надо напишите 'нет'\nВетчина,Больше сыра,Маслины,Пепперони,Филе цыпленка")
            if add_ingred_choice == 'нет':
                pizza_menu = PizzaMenu(user_choice, self.menu)
                pizza_menu.choice_pizza()
                json_work = WorkWithJson(pizza_menu.pizza_menu_json_key(), pizza_menu.pizza_menu_json_value())
                json_work.create_json()
            else:
                pizza_own = PizzaOwn(user_choice, add_ingred_choice, self.menu)
                pizza_own.choice_pizza()
                pizza_own.get_add_ingred()
                json_work = WorkWithJson(pizza_own.pizza_own_json_key(), pizza_own.pizza_own_json_value())
                json_work.create_json()

    def show_json(self):
        import json
        try:
            with open('Pizza_and_order.json', 'r', encoding='utf-8') as fp:
                pizza_list = json.load(fp)
            print()
            print('Список проданных пицц')
            print(pizza_list)
            print(f'Количество проданных пицц - {len(pizza_list)}')
            order = 0
            for i in pizza_list:
                for key in i:
                    order += int(i[key])
            print(f'Выручка - {order}')

        except JSONDecodeError:
            print('Пока еще нет проданных пицц')


class WorkWithJson:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def find_json(self):
        find_json = []
        try:
            with open('Pizza_and_order.json', 'r', encoding='utf-8') as fp:
                find_json = load(fp)
        except JSONDecodeError:
            find_json = 'Error'
        return find_json

    def create_json(self):
        json_data = []
        data = {}
        data[self.key] = self.value
        json_data.append(data)
        if self.find_json() == 'Error':
            with open('Pizza_and_order.json', 'w', encoding='utf-8') as fp:
                dump(json_data, fp, ensure_ascii=False, indent=2)
        elif self.find_json() != 'Error':
            with open('Pizza_and_order.json', 'r', encoding='utf-8') as fp:
                self.json_data = load(fp)
            self.add_json()

    def add_json(self):
        data = {}
        data[self.key] = self.value
        self.json_data.append(data)
        with open('Pizza_and_order.json', 'w', encoding='utf-8') as fp:
            dump(self.json_data, fp, ensure_ascii=False, indent=2)


class PizzaMenu:

    def __init__(self, user_choice, menu):
        self.menu = menu
        self.user_choice = user_choice

    def choice_pizza(self):
        print(f'Вы заказали пиццу {self.user_choice}')
        return self.user_choice

    def pizza_menu_json_key(self):
        return self.user_choice

    def pizza_menu_json_value(self):
        return self.menu[self.user_choice][1]


class PizzaOwn:
    def __init__(self, user_choice, ingred_choice, menu):
        self.menu = menu
        self.ingred_choice = ingred_choice
        self.user_choice = user_choice

    def choice_pizza(self):
        print(f'Вы заказали пиццу {self.user_choice}')
        return self.user_choice

    def get_add_ingred(self):
        print(f'Добавки:{self.ingred_choice}')

    def pizza_own_json_key(self):
        return f'{self.user_choice},Добавки:{[self.ingred_choice]}'

    def pizza_own_json_value(self):
        return self.menu[self.user_choice][1]


class PizzaUser:
    def __init__(self, user_ingred, ingred_order):
        self.user_ingred = user_ingred
        self.ingred_order = ingred_order

    def get_user_pizza(self):
        user_pizza = {}
        user_pizza['User Pizza'] = self.user_ingred
        print(f'Вы заказали {user_pizza}')

    def pizza_user_json_key(self):
        return f'User_Pizza: {self.user_ingred}'

    def pizza_user_json_value(self):
        return self.user_pizza_order()

    def user_pizza_order(self):
        order = 0
        for i in self.user_ingred.split():
            if i in self.ingred_order:
                order += self.ingred_order[i]
        return order