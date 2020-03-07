from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from account.forms import SignUpForm


def register(request):
    if (request.method == 'POST'):
        form = SignUpForm(request.POST)
        if (form.is_valid()):
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
