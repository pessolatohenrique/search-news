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
    def build_timeline(categories, sites):
        timeline_list = []
        for category in categories:
            for site in sites:
                news_list = site.search(category)

                for news in news_list:
                    timeline_list.append(news)

        return timeline_list
