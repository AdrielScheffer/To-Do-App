from dataclasses import fields
from re import template
from turtle import mode
from unittest import mock
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from tasks.models import Tasks
# Create your views here.

class Index(ListView):
    model= Tasks
    template_name ='index.html'
    ordering = ['-date_created']


class Create_tasks(CreateView):
    model = Tasks
    fields = '__all__'
    template_name = 'create_task.html'


class Eliminate_task(DeleteView):
    model = Tasks
    template_name = 'delete_task.html'
    success_url = reverse_lazy('home')  
    

