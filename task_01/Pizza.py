from __future__ import annotations
from json import load, dump, JSONDecodeError

class MenuAndAdd:
    def __init__(self):
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
                        "пицца-соус":50,
                        "соус-тысяча-островов":50,
                        "ветчина": 50,
                        "филе-цыпленка": 50,
                        "ананас": 50,
                        "пепперони": 50,
                        "сыр-моцарелла": 50,
                        "тунец": 50,
                        "маслины": 50,
                        "базилик": 50,
                        "свежие-томаты": 50,
                        "свежие-шампиньоны": 50,}
    def get_menu(self,menu):
        menu_list = []
        for i in menu.keys():
            menu_list.append(i)
        return menu_list

    def get_ingred(self):
        ingred_list = []
        for i in self.ingred_order.keys():
            ingred_list.append(i)
        return ingred_list

class WorkWithJson:
    def __init__(self,key,value):
        self.key = key
        self.value = value

    def find_json(self):
        find_json = []
        try:
            with open('Pizza_and_order.json','r',encoding = 'utf-8') as fp:
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
            with open('Pizza_and_order.json','w',encoding = 'utf-8') as fp:
                dump(json_data,fp,ensure_ascii=False,indent = 2)
        elif self.find_json() != 'Error':
            with open('Pizza_and_order.json','r',encoding = 'utf-8') as fp:
                self.json_data = load(fp)
            self.add_json()

    def add_json(self):
        data = {}
        data[self.key] = self.value
        self.json_data.append(data)
        with open('Pizza_and_order.json','w',encoding = 'utf-8') as fp:
            dump(self.json_data,fp,ensure_ascii=False,indent = 2)

class PizzaMenu:

    def __init__(self,user_choice,menu):
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
    def __init__(self,user_choice,ingred_choice,menu):
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
    def __init__(self,user_ingred,ingred_order):
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
