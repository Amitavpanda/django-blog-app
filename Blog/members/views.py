from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy


# Create your views here.
class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = './registration/register.html'
    success_url = reverse_lazy('login')

