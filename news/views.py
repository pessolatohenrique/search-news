from django.shortcuts import render
from django.http import HttpResponse
from subject.models import Subject
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    user = User.objects.get(id=2)

    categories = Subject.objects.filter(users=user).order_by('name')
    return render(request, 'index.html', {
        'categories': categories
    })
