import json
class FilmModel:

    def __init__(self,name_film,genre,director,year,duration,film_studio):
        self.name_film = name_film
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.film_studio = film_studio
        self.film_inform = []
        self.film_actors = []



    def data_package(self):
        data_film = {}
        data_film['Название фильма'] = self.name_film
        data_film['Жанр'] = self.genre
        data_film['Режиссер'] = self.director
        data_film['Год выпуска'] = self.year
        data_film['Длительность'] = self.duration
        data_film['Студия'] = self.film_studio
        self.film_inform.append(data_film)
        return data_film


    def actors_data(self,actor,role):
        data_actors = {}
        data_actors[f"Актер - {actor}"] = f'Роль - {role}'
        self.film_inform.append(data_actors)
        self.film_actors.append(data_actors)

    def get_film_inform(self):
        return self.data_package(),self.get_film_actors()

    def get_film_actors(self):
        return self.film_actors

    def json_package(self,film_name):
        with open(f'{film_name}.json', 'w', encoding = 'utf-8') as fp:
            json.dump(self.film_inform,fp,ensure_ascii=False,indent = 2)

