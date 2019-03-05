# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def settings(request):
    if request.method == "POST":
        return render(request, 'home.html', {})
    else:
        return render(request, 'settings.html', {})
