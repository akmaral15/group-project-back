from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=900)

class Food(models.Model):
    name = models.CharField(max_length=900)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    price = models.FloatField()
    description = models.CharField(max_length=900)
    ingredients = models.CharField(max_length=900)
    images = models.CharField(max_length=900)

class User(models.Model):
    usename = models.TextField()
    email = models.TextField()
    password = models.TextField()
class Manager(models.Model):
    usename = models.TextField()
    email = models.TextField()
    password = models.TextField()
    