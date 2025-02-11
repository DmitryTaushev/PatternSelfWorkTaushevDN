from Pizza import PizzaMenu, PizzaOwn,PizzaUser


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
            pizza_menu = PizzaMenu(user_choice)
            pizza_menu.choice_pizza()
            pizza_menu.create_json()
        else:
            pizza_own = PizzaOwn(user_choice,add_ingred_choice)
            pizza_own.choice_pizza()
            pizza_own.create_json()
            pizza_own.get_add_ingred()



