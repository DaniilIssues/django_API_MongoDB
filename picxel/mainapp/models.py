from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=70)


class Image(models.Model):
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    source = models.CharField(max_length=70, null=True)
    size = models.CharField(max_length=70)
    author = models.CharField(max_length=70, null=True, blank=True)
    license = models.CharField(max_length=70, null=True, blank=True)
    pic_original = models.ImageField(upload_to='orig/', null=True)
    pic_min = models.ImageField(upload_to='min/', null=True)
