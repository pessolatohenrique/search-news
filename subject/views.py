from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Subject

# Create your views here.


@login_required(login_url='/login/')
def index(request):
    categories = Subject.objects.filter(users=request.user).order_by('name')
    return render(request, 'subject/index.html', {'categories': categories})


@login_required(login_url='/login/')
def delete(request):
    if (request.method == 'POST'):
        subject_user = Subject.objects.filter(
            id=request.POST['subject_id']).get()

        subject_user.users.remove(request.user)
        print(subject_user.users.all())

    return redirect('index')
