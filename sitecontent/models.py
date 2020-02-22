from django.db import models

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
