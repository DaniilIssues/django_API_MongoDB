from django.shortcuts import render
from rest_framework import viewsets
from mainapp.serializers import ImageSerializer, CategorySerializer, TagSerializer
from mainapp.models import Image, Tag, Category
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer, JSONRenderer])
def main(request):
    queryset = Image.objects.all()

    if request.accepted_renderer.format == 'html':
        data = {'users': queryset}
        return Response(data, template_name='mainapp/index.html')

    serializer = ImageSerializer(instance=queryset)
    data = serializer.data
    return Response(data)
