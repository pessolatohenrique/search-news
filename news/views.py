from django.shortcuts import render
from django.http import HttpResponse
from subject.models import Subject
from sitecontent.models import Site
from news.models import News
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    user = User.objects.get(id=2)

    categories = Subject.objects.filter(users=user).order_by('name')
    categories_timeline = categories[0:3]
    sites = Site.objects.filter(id=2).order_by('name').all()
    timeline = News.build_timeline(categories_timeline, sites)

    return render(request, 'index.html', {
        'categories': categories,
        'timeline': timeline
    })
