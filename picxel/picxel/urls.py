from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import mainapp.views as main
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'image', main.ImageViewSet)
router.register(r'category', main.CategoryViewSet)
router.register(r'tag', main.TagViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', main.ImagesListView.as_view(), name='main'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
