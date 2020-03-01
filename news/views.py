from django.shortcuts import render
from django.http import HttpResponse
from subject.models import Subject
from sitecontent.models import Site
from news.models import News
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/login/')
def index(request):
    user = User.objects.get(id=request.user.id)

    categories = Subject.objects.filter(users=user).order_by('name')
    categories_timeline = categories[0:3]
    sites = Site.objects.filter(id=2).order_by('name').all()
    timeline = News.build_timeline(categories_timeline, sites)

    return render(request, 'index.html', {
        'categories': categories,
        'timeline': timeline
    })


@login_required(login_url='/login/')
def search(request):
    category_id = request.GET.get('id')
    site_id = request.GET.get('site_id')
    user = User.objects.get(id=request.user.id)

    categories = Subject.objects.filter(users=user).order_by('name')
    sites = Site.objects.order_by('name')
    current_category = Subject.objects.get(id=category_id)
    current_site = Site.objects.get(id=site_id)
    timeline = News.build_from_category(current_category, current_site)

    print(site_id)

    return render(request, 'category.html', {
        'categories': categories,
        'sites': sites,
        'current_category': current_category,
        'current_site': site_id,
        'timeline': timeline
    })


@login_required(login_url='/login/')
def view(request, id):
    user = User.objects.get(id=request.user.id)

    categories = Subject.objects.filter(users=user).order_by('name')
    sites = Site.objects.order_by('name')
    current_category = Subject.objects.get(id=id)
    current_site = Site.objects.get(id=2)
    timeline = News.build_from_category(current_category, current_site)

    return render(request, 'category.html', {
        'categories': categories,
        'sites': sites,
        'current_category': current_category,
        'current_site': current_site.id,
        'timeline': timeline
    })
