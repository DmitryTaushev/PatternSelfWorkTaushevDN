class ArticleView:

    def __init__(self,article_control):
        self.article_control = article_control

    def display_default_action(self):
        print(self.article_control.get_default_action())

    def display_article_inform_auth(self,user_role = 'user'):
        result = self.article_control.get_article_inform(user_role)
        if result == 'Forbidden!':
            print(result)
        else:
            return self.article_control.get_article_inform()

    def display_article_name(self):
        return self.article_control.get_article_name()

    def display_author_name(self):
        return self.article_control.get_author_name()

    def display_count_art(self):
        return self.article_control.get_count_art()

    def display_publisher(self):
        return self.article_control.get_publisher()

    def display_brief_desc(self):
        return self.article_control.get_brief_desc()