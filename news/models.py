from django.db import models

# Create your models here.


class News():
    def __init__(self, figure_url, title, published_at, subject, site):
        self.figure_url = figure_url
        self.title = title
        self.published_at = published_at
        self.subject = subject
        self.site = site

    @staticmethod
    def build_timeline(categories, sites) -> list:
        """constrói a lista de timeline do site 

        Arguments:
            categories {list} -- categorias a serem percorridas
            sites {list} -- sites a serem percorridos

        Returns:
            list -- lista com as principais notícias encontradas
        """
        timeline_list = []
        for category in categories:
            for site in sites:
                news_list = site.search(category)

                for news in news_list:
                    timeline_list.append(news)

        return timeline_list

    @staticmethod
    def build_from_category(category, site) -> list:
        """constrói a lista de notícias de acordo com uma categoria

        Arguments:
            category {object} -- dados de uma categoria
            site {object} -- dados de um site

        Returns:
            list -- lista com as principais notícias encontradas
        """
        timeline_list = []
        news_list = site.search(category)

        for news in news_list:
            timeline_list.append(news)

        return timeline_list
