from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=70)


class Tags(models.Model):
    name = models.CharField(max_length=70)


class Image(models.Model):
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    source = models.CharField(max_length=70)
    author = models.CharField(max_length=70)
    license = models.CharField(max_length=70)
    pic = models.ImageField(upload_to='pic/')
