# encoding:utf8
from __future__ import unicode_literals
from operator import itemgetter
from itertools import groupby

from django.forms.models import model_to_dict

from django.shortcuts import render, render_to_response
from models import Article, Product, ProductCategory, ProductSet, Image
from django.conf import settings
# Create your views here.

IMAGE_API_HOST = settings.IMAGE_HOST


def index(request):
    return render_to_response("index.html", locals())


def aboutus(request):
    return render_to_response("aboutus.html", locals())


def contact(request):
    return render_to_response("contact.html", locals())


def joinus(request):
    return render_to_response("joinus.html", locals())


def news_detail(request):
    article_id = int(request.GET.get("article_id"))
    article = Article.objects.get(id=article_id)
    return render_to_response("news_detail.html", locals())


def get_short_content(value):
    value.content = value.content[:60] + '...'

    try:
        print value.id
        image = Image.objects.get(article_id=value.id)
        value.src = IMAGE_API_HOST + image.file_name
        print value.src
    except Image.DoesNotExist, e:
        print "ddd"
        value.src = ''
    return value


def news(request):
    news_list = map(get_short_content, Article.objects.all().order_by('-id'))
    return render_to_response("news.html", locals())


def getproductList(category_id):
    category1 = ProductCategory.objects.get(id=category_id)
    c_products = Product.objects.filter(category=category1)
    renderlist = []
    item = {}
    for pro in c_products:
        try:
            print pro.id
            image1 = Image.objects.get(product_id=pro.id)
            pro.src = IMAGE_API_HOST + image1.file_name
        except Image.DoesNotExist, e:
            print "ddd"
            pro.src = ''
        # print type(pro)
        # model_to_dict(pro)
        tmpProDict = {}
        tmpProDict['id'] = pro.id
        tmpProDict['name'] = pro.name
        tmpProDict['src'] = pro.src
        tmpProDict['set_id'] = pro.pset.id
        tmpProDict['set_name'] = pro.pset.name
        tmpProDict['set_en_name'] = pro.pset.english_name
        # print tmpProDict
        renderlist.append(tmpProDict)
    renderlist.sort(key=itemgetter('set_name'))
    product_list = []
    for set_name, items in groupby(renderlist, key=itemgetter('set_name')):

        local_items = [i for i in items]
        product_list.append({
            "set_name": set_name,
            "set_en_name": local_items[0]["set_en_name"],
            "products": local_items
        })

    return product_list

def product(request):
    category_id = int(request.GET.get("category_id", 0))
    print category_id
    categories = map(
        lambda x: x, ProductCategory.objects.all().order_by('-id'))

    if not category_id:
        category_id = categories[0].id
        categories[0].active = True
        print categories[0].active
        # category1 = ProductCategory.objects.get(id=category_id)
        # c_products = Product.objects.filter(category=category1)
        # renderlist = []
        # item = {}
        # for pro in c_products:
        #     try:
        #         print pro.id
        #         image1 = Image.objects.get(product_id=pro.id)
        #         pro.src = IMAGE_API_HOST + image1.file_name
        #     except Image.DoesNotExist, e:
        #         print "ddd"
        #         pro.src = ''
        #     # print type(pro)
        #     # model_to_dict(pro)
        #     tmpProDict = {}
        #     tmpProDict['id'] = pro.id
        #     tmpProDict['name'] = pro.name
        #     tmpProDict['src'] = pro.src
        #     tmpProDict['set_id'] = pro.pset.id
        #     tmpProDict['set_name'] = pro.pset.name
        #     tmpProDict['set_en_name'] = pro.pset.english_name
        #     # print tmpProDict
        #     renderlist.append(tmpProDict)
        # renderlist.sort(key=itemgetter('set_name'))
        # product_list = []
        # for set_name , items in groupby(renderlist, key=itemgetter('set_name')):

        #     local_items = [i for i in items]
        #     product_list.append({
        #         "set_name": set_name,
        #         "set_en_name": local_items[0]["set_en_name"],
        #         "products": local_items
        #     })
            
        # print product_list
        product_list = getproductList(category_id)
        # print product_list
        return render_to_response("product.html", locals())
    else:
        tmpCategories = []
        for cate2 in categories:
            if cate2.id == category_id:
                cate2.active = True
            tmpCategories.append(cate2)
        categories = tmpCategories
        product_list = getproductList(category_id)
        # print product_list
        return render_to_response("product.html", locals())
