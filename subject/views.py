from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Subject
from .forms import SubjectForm

# Create your views here.


@login_required(login_url='/login/')
def index(request):
    categories = Subject.objects.filter(users=request.user).order_by('name')
    return render(request, 'subject/index.html', {'categories': categories})


def custom_create(request, form):
    object_exists = Subject.objects.filter(
        name=form.cleaned_data['name']).exists()

    if (object_exists):
        subject = Subject.objects.filter(
            name=form.cleaned_data['name']).get()

    if(not object_exists):
        subject = Subject()
        subject.name = form.cleaned_data['name'].capitalize()
        subject.save()

    subject.users.add(request.user)
    subject.save()


@login_required(login_url='/login/')
def create(request):
    if (request.method == 'POST'):
        form = SubjectForm(request.POST)

        if (form.is_valid()):
            custom_create(request, form)
            return redirect('subject_index')
    else:
        form = SubjectForm()

    return render(request, 'subject/form.html', {'form': form})


@login_required(login_url='/login/')
def delete(request):
    if (request.method == 'POST'):
        subject_user = Subject.objects.filter(
            id=request.POST['subject_id']).get()

        subject_user.users.remove(request.user)

    return redirect('subject_index')
