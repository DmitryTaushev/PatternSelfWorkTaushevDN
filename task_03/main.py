from task_03.Model import FilmModel
from task_03.View import FilmView
from task_03.Controller import FilmController

if __name__ == '__main__':
    film_model = FilmModel("Назад в будущее","Фантастика","Роберт Земекис","1985","1 ч 56 мин","Universal Pictures")
    film_control = FilmController(film_model)
    film_view = FilmView(film_control)
    film_model.actors_data("Майкл Джей Фокс", "Марти Макфлай")
    film_model.actors_data("Кристофер Ллойд", "Доктор Эмметт Браун")
    film_model.actors_data("Лиа Томпсон", "Лоррейн Макфлай")
    film_model.actors_data("Криспин Гловер", "Джордж Макфлай")

    film_view.display_default_action()
    print(film_view.display_film_inform_auth('user'))
    film_view.display_film_name()
    film_view.display_genre()
    film_view.display_director()
    film_view.display_year()
    film_view.display_duration()
    film_view.display_film_studio()
    print(film_view.display_actors())
    print()

