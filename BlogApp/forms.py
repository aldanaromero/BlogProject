from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from BlogApp.models import Blog, Profile


class NewBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'subtitle', 'body', 'date', 'picture']
        ##fields = ['title', 'subtitle', 'body', 'owner', 'date', 'picture']
        widgets = {
            'date': forms.DateInput(format='%d/%m/%Y'),
            #   'owner': forms.TextInput(attrs={'value': '', 'id': 'owner_id', 'type': 'hidden'}),
            ## REVISAR
        }
        labels = {
            'title': 'Título',
            'subtitle': 'Subtítulo',
            'body': 'Contenido',
            #  'owner': 'Autor',
            'date': 'Fecha de creación',
            'picture': 'Imagen',
        }


class UpdateBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'subtitle', 'body', 'picture']
        labels = {
            'title': 'Título',
            'subtitle': 'Subtítulo',
            'body': 'Contenido',
            'picture': 'Imagen',
        }


class UserRegister(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput)
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


class UpdateUser(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nombre', widget=forms.TextInput)
    last_name = forms.CharField(label='Apellido', widget=forms.TextInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture', 'description', 'link']
