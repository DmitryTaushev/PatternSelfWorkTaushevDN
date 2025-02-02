class FilmController:

    def __init__(self,film_model):
        self.film_model = film_model

    def get_default_action(self):
        return "Добро пожаловать на главную страницу!"

    def get_film_inform(self,user_role = 'user'):
        if user_role in ['admin','user']:
            if self.film_model.get_film_inform():
                return self.film_model.get_film_inform()
        else:
            return 'Forbidden!'


    def get_film_name(self):
        data = self.film_model.data_package()
        if data:
            for key in data:
                if key == 'Название фильма':
                    print(data['Название фильма'])

    def get_genre(self):
        data = self.film_model.data_package()
        if data:
            for key in data:
                if key == 'Жанр':
                    print(data['Жанр'])

    def get_director(self):
        data = self.film_model.data_package()
        if data:
            for key in data:
                if key == 'Режиссер':
                    print(data['Режиссер'])

    def get_year(self):
        data = self.film_model.data_package()
        if data:
            for key in data:
                if key == 'Год выпуска':
                    print(data['Год выпуска'])

    def get_duration(self):
        data = self.film_model.data_package()
        if data:
            for key in data:
                if key == 'Длительность':
                    print(data['Длительность'])

    def get_film_studio(self):
        data = self.film_model.data_package()
        if data:
            for key in data:
                if key == 'Студия':
                    print(data['Студия'])

    def get_actors(self):
        return self.film_model.get_film_actors()





