from django.views.generic import ListView
from rest_framework import viewsets
from mainapp.serializers import ImageSerializer, CategorySerializer, TagSerializer
from mainapp.models import Image, Tag, Category
from PIL import Image as Imag
from django.conf import settings
import os


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ImagesListView(ListView):
    model = Image
    paginate_by = 20
    template_name = 'mainapp/index.html'


