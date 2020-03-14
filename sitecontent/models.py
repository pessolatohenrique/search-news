from django.db import models
from news.models import News
import requests
from bs4 import BeautifulSoup


# Create your models here.


class Site(models.Model):
    name = models.CharField(max_length=200, unique=True)
    url = models.CharField(max_length=200, unique=True)
    container_class = models.CharField(max_length=200)
    title_class = models.CharField(max_length=200)
    tag_title = models.CharField(max_length=200, blank=True)
    published_class = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_url_search(self, subject) -> str:
        """obtem a url de pesquisa, de acordo com um assunto

        Arguments:
            subject {string} -- assunto pesquisado

        Returns:
            str -- url completa, incluindo o assunto pesquisado
        """

        str_search = '{}?q={}'.format(self.url, subject)
        return str_search

    def get_figure_url(self, news) -> str:
        """obtem a URL para imagem de uma notícia

        Arguments:
            news {object} -- contém informações gerais de uma notícia

        Returns:
            str -- [str] URL de imagem da notícia
        """
        figure = news.find('img')
        figure_url = '#N/D'

        if (figure is not None):
            figure_url = news.find('img').get('src')

            if (figure_url == None):
                figure_url = news.find('img').get('data-src')

        return figure_url

    def get_title(self, news) -> str:
        """obtém o título da notícia

        Arguments:
            news {object} -- contém informações gerais de uma notícia 

        Returns:
            str -- título da notícia
        """
        title = news.find(class_=self.title_class)

        if (self.tag_title):
            title = title.find(self.tag_title)

        title = title.contents[0]

        return title

    def search(self, subject) -> list:
        """pesquisa notícias de acordo com o assunto especificado

        Arguments:
            subject {string} -- assunto pesquisado

        Returns:
            list -- lista de notícias encontradas
        """
        url = self.get_url_search(subject)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')

        container_list = soup.find_all(class_=self.container_class)
        news_list = []

        for news in container_list:
            figure_url = self.get_figure_url(news)
            title = self.get_title(news)
            published_at = news.find(class_=self.published_class).contents[0]

            founded = News(figure_url, title, published_at, subject, self.name)

            news_list.append(founded)

        return news_list
