#encoding:utf8
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from models import Article
from django.conf import settings
# Create your views here.


def index(request):
    return render_to_response("index.html", locals())

def aboutus(request):
    return render_to_response("aboutus.html", locals())

def contact(request):
    return render_to_response("contact.html", locals())

def joinus(request):
    return render_to_response("joinus.html", locals())

def news_detail(request):
    article_id =  int(request.GET.get("article_id"))
    article = Article.objects.get(id=article_id)
    return render_to_response("news_detail.html", locals())

def get_short_content(value):
    value.content = value.content[:60] + '...'
    IMAGE_API_HOST = settings.IMAGE_HOST
    value.src = IMAGE_API_HOST + value.image.file_name
    return value

def news(request):
    news_list = map(get_short_content, Article.objects.all().order_by('-id'))
    return render_to_response("news.html", locals())

def product(request):
    return render_to_response("product.html", locals())