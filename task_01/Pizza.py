from __future__ import annotations
from json import load, dump, JSONDecodeError


class PizzaMenu:

    def __init__(self,user_choice,menu):
        self.menu = menu
        self.user_choice = user_choice
    def choice_pizza(self):
        if self.user_choice == "Гавайская":
            print(f'Вы заказали пиццу {self.user_choice}')
            return self.user_choice
        elif self.user_choice == "Грибная":
            print(f'Вы заказали пиццу {self.user_choice}')
            return self.user_choice
        elif self.user_choice == "Пепперони":
            print(f'Вы заказали пиццу {self.user_choice}')
            return self.user_choice
        elif self.user_choice == "Сырный цыпленок":
            print(f'Вы заказали пиццу {self.user_choice}')
            return self.user_choice
        elif self.user_choice == "Тунец - тысяча островов":
            print(f'Вы заказали пиццу {self.user_choice}')
            return self.user_choice


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
        data[self.user_choice] = self.menu[self.user_choice][1]
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
        data[self.user_choice] = self.menu[self.user_choice][1]
        self.json_data.append(data)
        with open('Pizza_and_order.json','w',encoding = 'utf-8') as fp:
            dump(self.json_data,fp,ensure_ascii=False,indent = 2)



class PizzaOwn:
    def __init__(self,user_choice,ingred_choice,menu):
        self.menu = menu
        self.add_ingred_data = []
        self.ingred_choice = ingred_choice
        self.user_choice = user_choice

    def choice_pizza(self):
        if self.user_choice == "Гавайская":
            print(f'Вы заказали пиццу {self.user_choice}')
            return self.user_choice
        elif self.user_choice == "Грибная":
            print(f'Вы заказали пиццу {self.user_choice}')
            return self.user_choice
        elif self.user_choice == "Пепперони":
            print(f'Вы заказали пиццу {self.user_choice}')
            return self.user_choice
        elif self.user_choice == "Сырный цыпленок":
            print(f'Вы заказали пиццу {self.user_choice}')
            return self.user_choice
        elif self.user_choice == "Тунец - тысяча островов":
            print(f'Вы заказали пиццу {self.user_choice}')
            return self.user_choice

    def get_add_ingred(self):
        print(f'Добавки:{self.ingred_choice}')

    def find_json(self):
        try:
            with open('Pizza_and_order.json', 'r', encoding='utf-8') as fp:
                find_json = load(fp)
        except JSONDecodeError:
            find_json = 'Error'
        return find_json

    def create_json(self):
        json_data = []
        data = {}
        data[f'{self.user_choice},Добавки:{[self.ingred_choice]}'] = self.menu[self.user_choice][1]
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
        data[f'{self.user_choice},Добавки:{[self.ingred_choice]}'] = self.menu[self.user_choice][1]
        self.json_data.append(data)
        with open('Pizza_and_order.json', 'w', encoding='utf-8') as fp:
            dump(self.json_data, fp, ensure_ascii=False, indent=2)

class PizzaUser:
    def __init__(self,user_ingred):
        self.user_ingred = user_ingred


    def find_json(self):
        try:
            with open('Pizza_and_order.json', 'r', encoding='utf-8') as fp:
                find_json = load(fp)
        except JSONDecodeError:
            find_json = 'Error'
        return find_json

    def get_user_pizza(self):
        user_pizza = {}
        user_pizza['User Pizza'] = self.user_ingred
        print(f'Вы заказали {user_pizza}')

    def ingred_order(self):
        ingred_order = {"сырный-соус": 50,
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
                        "свежие-шампиньоны": 50,


        }
        return ingred_order

    def user_pizza_order(self):
        order = 0
        for i in self.user_ingred.split():
            if i in self.ingred_order():
                order += self.ingred_order()[i]
        return order

    def create_json(self):
        json_data = []
        data = {}
        order_data = {}
        order_data[self.user_ingred] = int(self.user_pizza_order())
        data['User_Pizza'] = order_data
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
        order_data = {}
        order_data[self.user_ingred] = int(self.user_pizza_order())
        data['User_Pizza'] = order_data
        self.json_data.append(data)
        with open('Pizza_and_order.json', 'w', encoding='utf-8') as fp:
            dump(self.json_data, fp, ensure_ascii=False, indent=2)