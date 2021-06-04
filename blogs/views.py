from django import forms
from blogs.forms import RegisterForm
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
            user = User.objects.create_superuser(
                username=cleaned_data.get('username'),
                password=cleaned_data.get('password'),
                email=cleaned_data.get('email'),
                first_name=cleaned_data.get('first_name'),
                last_name=cleaned_data.get('last_name')
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


