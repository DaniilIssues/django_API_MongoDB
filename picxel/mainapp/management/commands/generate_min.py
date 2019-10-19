import os

from django.core.management.base import BaseCommand
from mainapp.models import Category, Tag, Image
from PIL import Image as ImagePIL

from picxel.settings import BASE_DIR


class Command(BaseCommand):
    def handle(self, *args, **options):
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        images = Image.objects.all()
        for image in images:
            try:
                with open(f"{MEDIA_ROOT}/{image.pic_original}", 'rb') as fp:
                    im = ImagePIL.open(fp)
                    min_im = im.resize((512, 512))
                    name = image.pic_original.name.replace("orig/", '')
                    name = f"{MEDIA_ROOT}/min/{name}"
                    new = min_im.save(name)
            except FileNotFoundError:
                print("error")
                continue
