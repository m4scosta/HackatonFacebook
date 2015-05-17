# coding: utf-8
from django.shortcuts import render
from HackatonFacebook.views import HOME_TEMPLATE

__author__ = 'bustamante'


def home(request):
    return render(request, HOME_TEMPLATE)
