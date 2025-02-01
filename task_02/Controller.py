class ArticleController:

    def __init__(self,article_model):
        self.article_model = article_model

    def get_default_action(self):
        return "Добро пожаловать на главную страницу!"

    def get_article_inform(self,user_role = 'user'):
        if user_role in ['admin','user']:
            if self.article_model.get_art_inform():
                return self.article_model.get_art_inform()
            return None
        return 'Forbidden!'

    def get_article_name(self):
        data = self.article_model.get_art_inform()
        if data:
            for key in data:
                if key == 'Название статьи':
                    print(data['Название статьи'])

    def get_author_name(self):
        data = self.article_model.get_art_inform()
        if data:
            for key in data:
                if key == 'Автор статьи':
                    print(data['Автор статьи'])

    def get_count_art(self):
        data = self.article_model.get_art_inform()
        if data:
            for key in data:
                if key == 'Количество знаков':
                    print(data['Количество знаков'])

    def get_publisher(self):
        data = self.article_model.get_art_inform()
        if data:
            for key in data:
                if key == 'Название издательства':
                    print(data['Название издательства'])

    def get_brief_desc(self):
        data = self.article_model.get_art_inform()
        if data:
            for key in data:
                if key == 'Краткое описание':
                    print(data['Краткое описание'])



