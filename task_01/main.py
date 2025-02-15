from Pizza import MenuAndAdd


if __name__ == "__main__":
    identification = input("Идентифицируйте себя: 'Admin','User'")
    menu_and_add = MenuAndAdd(identification)
    menu_and_add.admin_or_user()
    menu_and_add.user_choise()
    menu_and_add.show_json()