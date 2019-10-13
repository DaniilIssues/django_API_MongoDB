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
    paginate_by = 18
    template_name = 'mainapp/index.html'


# @api_view(['GET'])
# @renderer_classes([TemplateHTMLRenderer, JSONRenderer])
# def main(request, page=1):
#     queryset = Image.objects.all()
#
#     if request.accepted_renderer.format == 'html':
#         paginator = Paginator(queryset, 20)
#         try:
#             image_paginator = paginator.page(page)
#         except PageNotAnInteger:
#             image_paginator = paginator.page(1)
#         except EmptyPage:
#             image_paginator = paginator.page(paginator.num_pages)
#         data = {'images': image_paginator}
#         return Response(data, template_name='mainapp/index.html')
#
#     serializer = ImageSerializer(instance=queryset)
#     data = serializer.data
#     return Response(data)
