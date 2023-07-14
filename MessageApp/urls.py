from django.contrib.auth.views import LogoutView
from django.urls import path

from BlogApp.views import Pages, AddBlog, BlogDetail, Login, Register, UpdateBlog, UpdateUser, Profile, UpdateProfile
from MessageApp.views import NewMessage, AddMessage, Messages, MessageDetail

urlpatterns = [
    path('messages/', Messages.as_view(), name='messages'),
    path('add_message/', AddMessage.as_view(), name='new_message'),
    path('message/<int:pk>/', MessageDetail.as_view(), name='message'),
]
