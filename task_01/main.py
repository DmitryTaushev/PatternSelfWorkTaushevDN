from json import JSONDecodeError

from Pizza import PizzaMenu, PizzaOwn,PizzaUser, WorkWithJson, MenuAndAdd
import json

if __name__ == "__main__":
    menu_and_add = MenuAndAdd()
    menu = []
    identification = input("Идентифицируйте себя: 'Admin','User'")
    if identification == 'Admin':
        change_menu = input('Желаете ли изменить меню')
        if change_menu == 'да':
            print("1.Удалить позицию\n2.Добавить позицию\n")
            choice = input('Выберите желаемое действие')
            if choice == '1':
                del_position = input('Что желаете убрать?')
                del menu_and_add.menu[del_position]
                print(menu_and_add.menu)
                menu.append(menu_and_add.menu)
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
                menu_and_add.menu[name] = pizza_list_admin
                print(menu_and_add.menu)
                menu.append(menu_and_add.menu)
    elif identification == 'User':
        menu = menu_and_add.menu
        pass
    user_choice = input(f"Выберите пиццу\nEсли хотите собрать свою, напишите Своя пицца:{menu}")
    if user_choice == "Своя пицца":
        """Ингредиенты вводить через пробел и ингредиенты из двух слов вводить через тире """
        user_ingred = input(f"Выберите ингредиенты для своей пиццы:\n{menu_and_add.get_ingred()}")
        pizza_user = PizzaUser(user_ingred,menu_and_add.ingred_order)
        pizza_user.get_user_pizza()
        json_work = WorkWithJson(pizza_user.pizza_user_json_key(),pizza_user.pizza_user_json_value())
        json_work.create_json()

    else:
        add_ingred_choice = input(
                "Выберите добавки, если не надо напишите 'нет'\nВетчина,Больше сыра,Маслины,Пепперони,Филе цыпленка")
        if add_ingred_choice == 'нет':
            pizza_menu = PizzaMenu(user_choice,menu_and_add.menu)
            pizza_menu.choice_pizza()
            json_work = WorkWithJson(pizza_menu.pizza_menu_json_key(), pizza_menu.pizza_menu_json_value())
            json_work.create_json()
        else:
            pizza_own = PizzaOwn(user_choice,add_ingred_choice,menu_and_add.menu)
            pizza_own.choice_pizza()
            pizza_own.get_add_ingred()
            json_work = WorkWithJson(pizza_own.pizza_own_json_key(), pizza_own.pizza_own_json_value())
            json_work.create_json()
try:
    with open('Pizza_and_order.json','r',encoding = 'utf-8') as fp:
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

