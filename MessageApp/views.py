from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from MessageApp.forms import NewMessage
from MessageApp.models import Message


# Create your views here.

class AddMessage(LoginRequiredMixin, CreateView):
    model = Message
    form_class = NewMessage
    success_url = reverse_lazy('messages')
    template_name = 'addMessage.html'

    def form_valid(self, form):
        form.instance.from_user = self.request.user  # Asignar el usuario autenticado al campo 'owner'
        return super(AddMessage, self).form_valid(form)


class Messages(LoginRequiredMixin, ListView):
    context_object_name = 'messages'
    template_name = 'messages.html'
    login_url = 'accounts/login/'

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(to_user=user)

class MessageDetail(LoginRequiredMixin, DetailView):
    model = Message
    context_object_name = 'message'
    template_name = 'message.html'
