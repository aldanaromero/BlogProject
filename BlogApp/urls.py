from django.contrib.auth.views import LogoutView
from django.urls import path

from BlogApp.views import Pages, AddBlog, BlogDetail, Login, Register, UpdateBlog, UpdateUser, Profile, UpdateProfile, \
    Home, About

urlpatterns = [
    path('pages/', Pages.as_view(), name='pages'),
    path('add_page/', AddBlog.as_view(), name='new'),
    path('update_page/<int:pk>', UpdateBlog.as_view(), name='update'),
    path('page/<int:pk>/', BlogDetail.as_view(), name='page'),
    path('accounts/login/', Login.as_view(), name='login'),
    path('accounts/register/', Register.as_view(), name='register'),
    path('accounts/logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('update_user/<int:pk>', UpdateUser.as_view(), name='update_user'),
    path('update_profile/<int:pk>', UpdateProfile.as_view(), name='update_profile'),
    path('profile/<int:pk>', Profile.as_view(), name='profile'),
    path('home/', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='home'),

]