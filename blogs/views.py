from django.urls.base import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from blogs.models import Post
from django.core.mail import send_mail
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django import forms
from django.http.response import HttpResponse
from blogs.forms import ChangePasswordForm, RegisterForm, SubscribeForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.contenttypes.models import ContentType
from blogs.forms import RegisterForm
from django.contrib.auth.models import Permission, User
from django.http import Http404
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.views import View

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

def add_permission(request, username):
    """
    https://docs.djangoproject.com/en/3.2/topics/auth/default/#permission-caching

    myuser.groups.set([group_list])
    myuser.groups.add(group, group, ...)
    myuser.groups.remove(group, group, ...)
    myuser.groups.clear()
    myuser.user_permissions.set([permission_list])
    myuser.user_permissions.add(permission, permission, ...)
    myuser.user_permissions.remove(permission, permission, ...)
    myuser.user_permissions.clear()
    """
    user = get_object_or_404(User, username=username)
    content_type = ContentType.objects.get_for_model(Post)
    permission = Permission.objects.get(
        codename='view_post',
        content_type=content_type,
    )
    user.user_permissions.add(permission)
    return HttpResponse(user.has_perm('blogs.add_post'))


def add_post(request):
    user = request.user

    if user.has_perm('blogs.add_post'):
        Post.objects.create(title='Nambahin ah! hahahahaha hacker nih!')
        return HttpResponse("Hahahaha")
    else:
        return HttpResponse("Ups! anda tidak boleh nambahin data!")


# @login_required(login_url='/blogs/add-post/')
@permission_required('blogs.view_post', raise_exception=True)
def test_post(request):
    user = request.user

    # @permission_required('polls.add_choice', login_url='/loginpage/')
    # https://docs.djangoproject.com/en/3.2/topics/auth/default/#the-permission-required-decorator

    return HttpResponse("Hore")


class TestPost(PermissionRequiredMixin, View):
    permission_required = 'blogs.add_post'
    # raise_exception = True
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request):
        return HttpResponse("Hore")
    
    def post(self, request):
        return HttpResponse("Ini adalah post!")


def validate_jaroom(user):
    return user.email.endswith('@jayaabadi.com')


@user_passes_test(validate_jaroom, login_url='/admin/')
def ja_room(request):
    return HttpResponse('Selamat datang di Jaroom!')


class JARoom(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.email.endswith('@jayaabadi.com')

    def get(self, request):
        return HttpResponse("Hore")


def thanks(request):
    return HttpResponse("Thanks subscribe my blog!")


class SubscribeFormView(FormView):
    template_name = 'blogs/subscribe.html'
    form_class = SubscribeForm
    success_url = '/blogs/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        send_mail(
            'Thanks Subscribe!',
            'Lorem ipsum bla bla bla.',
            'admin@example.com',
            [form.cleaned_data.get('email')],
            fail_silently=False,
        )
        form.send_email()
        return super().form_valid(form)


class PostListView(ListView):
    model = Post
    paginate_by = 2  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = "Halo Dunia"
        return context

class PostCreateView(CreateView):
    model = Post
    fields = ['title']
    success_url = reverse_lazy('blogs:post-list')


class PostDetailView(DetailView):

    model = Post

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title']
    success_url = reverse_lazy('blogs:post-list')
    # template_name_suffix = '_update_form'


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blogs:post-list')

