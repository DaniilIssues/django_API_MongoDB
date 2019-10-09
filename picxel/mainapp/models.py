from django.db import models


class Tags(models.Model):
    tag = models.CharField(max_length=60)


class Picture(models.Model):
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    license = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    pic = models.ImageField(upload_to='pic/')
