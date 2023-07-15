from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, TemplateView

from BlogApp.forms import NewBlog, UserRegister, UpdateBlog, UpdateUser, UpdateProfile
from BlogApp.models import Blog
from BlogApp.models import Profile as ProfileModel


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class About(LoginRequiredMixin, TemplateView):
    template_name = 'about.html'


class Profile(LoginRequiredMixin, DetailView):
    model = ProfileModel
    context_object_name = 'profile'
    template_name = 'profile.html'


class Pages(LoginRequiredMixin, ListView):
    context_object_name = 'pages'
    queryset = Blog.objects.all()
    template_name = 'pages.html'
    login_url = '/accounts/login/'


class AddBlog(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = NewBlog
    success_url = reverse_lazy('pages')
    template_name = 'addBlog.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Asignar el usuario autenticado al campo 'owner'
        return super(AddBlog, self).form_valid(form)


class BlogDetail(LoginRequiredMixin, DetailView):
    model = Blog
    context_object_name = 'page'
    template_name = 'page.html'


class UpdateBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = UpdateBlog
    context_object_name = 'page'
    template_name = 'updateBlog.html'
    success_url = reverse_lazy('pages')


class Login(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        print(f'"{username}" login')
        return super().form_valid(form)

    def get_success_url(self):
        redirect_url = self.request.GET.get('next')
        if redirect_url:
            return redirect_url
        else:
            return '/home/'


class Register(CreateView):
    template_name = 'register.html'
    form_class = UserRegister
    success_url = reverse_lazy('login')

    ## Revisar
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)

            # Crear un perfil para el usuario registrado
            profile = ProfileModel.objects.create(user=user)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(Register, self).get(*args, **kwargs)


class UpdateUser(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UpdateUser
    context_object_name = 'user'
    template_name = 'updateUser.html'
    success_url = reverse_lazy('profile')

    def get_success_url(self):
        profile_id = self.request.user.id
        return reverse_lazy('profile', args=[profile_id])


class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = ProfileModel
    form_class = UpdateProfile
    context_object_name = 'profile'
    template_name = 'updateProfile.html'

    def get_success_url(self):
        profile_id = self.request.user.id
        return reverse_lazy('profile', args=[profile_id])
