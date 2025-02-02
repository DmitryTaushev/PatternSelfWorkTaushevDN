class FilmView:

    def __init__(self,film_control):
        self.film_control = film_control

    def display_default_action(self):
        print(self.film_control.get_default_action())

    def display_film_inform_auth(self,user_role = 'user'):
        result = self.film_control.get_film_inform(user_role)
        if result == 'Forbidden!':
            print(result)
        else:
            return self.film_control.get_film_inform()

    def display_film_name(self):
        return self.film_control.get_film_name()

    def display_genre(self):
        return self.film_control.get_genre()

    def display_director(self):
        return self.film_control.get_director()

    def display_year(self):
        return self.film_control.get_year()

    def display_duration(self):
        return self.film_control.get_duration()

    def display_film_studio(self):
        return self.film_control.get_film_studio()

    def display_actors(self):
        return self.film_control.get_actors()




