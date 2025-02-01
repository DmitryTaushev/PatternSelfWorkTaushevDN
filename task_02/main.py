from Model import ArticleModel
from Controller import ArticleController
from View import ArticleView

if __name__ == '__main__':
    article_model = ArticleModel('Об Искусственном Интеллекте',"Виктор Петров",1500,"Советский Полимер","О влиянии искусственного интеллекта на быт людей")
    article_control = ArticleController(article_model)
    article_view = ArticleView(article_control)

    article_view.display_default_action()
    print(article_view.display_article_inform_auth('user'))
    article_view.display_article_name()
    article_view.display_author_name()
    article_view.display_count_art()
    article_view.display_publisher()
    article_view.display_brief_desc()
    print()

    article_model = ArticleModel('О вкусных пирогах',"Сергей Нечаев",1000,"Советская кулинария","О правильном выборе температуры при приготовлении пирогов")
    article_control = ArticleController(article_model)
    article_view = ArticleView(article_control)

    article_model.json_package('Статья Сергея Нечаева')

    article_view.display_default_action()
    print(article_view.display_article_inform_auth('user'))
    print(article_view.display_article_inform_auth('П-3'))
    article_view.display_article_name()
    article_view.display_author_name()
    article_view.display_count_art()
    article_view.display_publisher()
    article_view.display_brief_desc()