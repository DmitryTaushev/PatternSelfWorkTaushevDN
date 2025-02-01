import json
class ArticleModel:

    def __init__(self,name_art,author_art,count_art,publisher,brief_desc):
        self.name_art = name_art
        self.author_art = author_art
        self.count_art = count_art
        self.publisher = publisher
        self.brief_desc = brief_desc

    def get_art_inform(self):
        return self.data_package()

    def data_package(self):
        data_art = {}
        data_art['Название статьи'] = self.name_art
        data_art['Автор статьи'] = self.author_art
        data_art['Количество знаков'] = self.count_art
        data_art['Название издательства'] = self.publisher
        data_art['Краткое описание'] = self.brief_desc
        return data_art

    def json_package(self,art_name):
        with open(f'{art_name}.json', 'w', encoding = 'utf-8') as fp:
            json.dump(self.data_package(),fp,ensure_ascii=False,indent = 2)
