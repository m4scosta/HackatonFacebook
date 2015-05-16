# coding: utf-8
from django.shortcuts import render
from HackatonFacebook.views.ajax import AJAX_TEMPLATE

__author__ = 'bustamante'


def home(request):
    context = {
        'title': 'Testando o Ajax',
        'button_name': 'Vamos pegar um nome com o Ajax?'
    }
    return render(request, AJAX_TEMPLATE, context)
