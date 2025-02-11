from Pizza import PizzaMenu, PizzaOwn,PizzaUser


pizza_menu = {
            "Гавайская": [100, 150, ["сырный соус", "ветчина", "филе цыпленка", "ананасы", "сыр моцарелла", "базилик"]],
            "Грибная": [100, 150, ["чесночный соус", "ветчина", "свежие шампиньоны", "сыр моцарелла", "базилик"]],
            "Пепперони": [100, 150, ["пицца - соус", "пепперони", "сыр моцарелла", "базилик"]],
            "Сырный цыпленок": [100, 150,
                                ["сырный соус", "филе цыпленка", "свежие томаты", "сыр моцарелла", "базилик"]],
            "Тунец - тысяча островов": [200, 300, ["соус тысяча островов", "тунец", "маслины", "сыр моцарелла", "лимон",
                                                   "базилик"]],
        }
identification = input("Идентифицируйте себя: 'Admin','User'")
if identification == 'Admin':
    change_menu = input('Желаете ли изменить меню')
    if change_menu == 'да':
        print("1.Удалить позицию\n2.Добавить позицию\n")
        choice = input('Выберите желаемое действие')
        if choice == '1':
            del_position = input('Что желаете убрать?')
            del pizza_menu[del_position]
            print(pizza_menu)


if __name__ == "__main__":
    user_choice = input("Выберите пиццу: Гавайская,Грибная,Пепперони,Сырный цыпленок,Тунец - тысяча островов,Своя пицца")
    if user_choice == "Своя пицца":
        """Ингредиенты вводить через пробел и ингредиенты из двух слов вводить через тире """
        user_ingred = input("Выберите ингредиенты для своей пиццы:\nсырный-соус чесночный-соус пицца-соус соус-тысяча-островов ветчина филе-цыпленка ананаc пепперони сыр-моцарелла тунец маслины базилик свежие-томаты свежие-шампиньоны")
        pizza_user = PizzaUser(user_ingred)
        pizza_user.get_user_pizza()
        pizza_user.create_json()
    else:
        add_ingred_choice = input(
                "Выберите добавки, если не надо напишите 'нет'\nВетчина,Больше сыра,Маслины,Пепперони,Филе цыпленка")
        if add_ingred_choice == 'нет':
            pizza_menu = PizzaMenu(user_choice,pizza_menu)
            pizza_menu.choice_pizza()
            pizza_menu.create_json()
        else:
            pizza_own = PizzaOwn(user_choice,add_ingred_choice,pizza_menu)
            pizza_own.choice_pizza()
            pizza_own.create_json()
            pizza_own.get_add_ingred()



