# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models


@python_2_unicode_compatible
class ProductCategory(models.Model):
    id = models.IntegerField(primary_key=True)     
    name = models.CharField(null=True, max_length=255)

    class Meta:
        db_table = "product_category"

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class ProductSet(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(null=True, max_length=255)
    english_name = models.CharField(null=True, max_length=255)

    class Meta:
        db_table = "product_set"

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Product(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(null=True, max_length=255)
    category = models.ForeignKey(ProductCategory, db_column="product_category_id") 
    pset = models.ForeignKey(ProductSet, db_column="set_id")

    # @property
    # def image(self):
    #     return Image.objects.get(product_id_id = self.id)
    
    class Meta:
        db_table = "product"

    def __str__(self):
        return self.name



# Create your models here.
@python_2_unicode_compatible
class Article(models.Model):

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, null=True)
    content = models.CharField(max_length=4096, null=True)
    comment = models.CharField(max_length=1024, null=True)
    like = models.IntegerField(default=0, null=True)
    created_at = models.IntegerField(null=True)

    class Meta:
        db_table = "article"

    def __str__(self):
        return self.title

    # @property
    # def image(self):
    #     return Image.objects.get(article_id_id = self.id)

@python_2_unicode_compatible
class Image(models.Model):
    id = models.IntegerField(primary_key=True)
    # product_id = models.ForeignKey(Product,db_column="product_id")
    product_id = models.IntegerField(null=True)
    file_name = models.CharField(max_length=255, null=True)
    # article_id = models.ForeignKey(Article, db_column='article_id')
    article_id = models.IntegerField(null=True)

    class Meta:
        db_table = "image"

    def __str__(self):
        return self.file_name
