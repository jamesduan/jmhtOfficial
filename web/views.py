# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

# Create your views here.


def index(request):
    return render_to_response("index.html", locals())

def aboutus(request):
    return render_to_response("index.html", locals())

def contact(request):
    return render_to_response("index.html", locals())

def joinus(request):
    return render_to_response("index.html", locals())

def news_detail(request):
    return render_to_response("index.html", locals())

def news(request):
    return render_to_response("index.html", locals())

def product(request):
    return render_to_response("index.html", locals())