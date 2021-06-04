from django import forms
from blogs.forms import ChangePasswordForm, RegisterForm
from django.shortcuts import redirect, render
from blogs.forms import RegisterForm
from django.contrib.auth.models import User
from django.http import Http404

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = None
            if cleaned_data.get('level') == "1":
                user = User.objects.create_superuser(
                    username=cleaned_data.get('username'),
                    password=cleaned_data.get('password'),
                    email=cleaned_data.get('email'),
                    first_name=cleaned_data.get('first_name'),
                    last_name=cleaned_data.get('last_name')
                )
            elif cleaned_data.get('level') == "2":
                user = User.objects.create_user(
                    username=cleaned_data.get('username'),
                    password=cleaned_data.get('password'),
                    email=cleaned_data.get('email'),
                    first_name=cleaned_data.get('first_name'),
                    last_name=cleaned_data.get('last_name'),
                    is_active=True,
                    is_staff=True,
                )
            elif cleaned_data.get('level') == "3":
                user = User.objects.create_user(
                    username=cleaned_data.get('username'),
                    password=cleaned_data.get('password'),
                    email=cleaned_data.get('email'),
                    first_name=cleaned_data.get('first_name'),
                    last_name=cleaned_data.get('last_name'),
                    is_active=True,
                    is_staff=False,
                )
            
            # TODO: Redirect ke halaman profile
            return redirect('blogs:profile', username=user.username)
        else:
            return render(request, 'blogs/register.html', {'form': form})
    
    else:
        form = RegisterForm()
        return render(request, 'blogs/register.html', {'form': form})


def profile(request, username):
    try:
        user = User.objects.get(username=username)
        print(user, username)
        return render(request, 'blogs/profile.html', {'user': user})
    except:
        raise Http404()


def change_password(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404()

    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user.set_password(cleaned_data.get('new_password'))
            user.save()
            return redirect('blogs:profile', username=user.username)
        else:
            return render(request, 'blogs/change_password.html', {'form': form})
    
    else:
        form = ChangePasswordForm()
        return render(request, 'blogs/change_password.html', {'form': form})