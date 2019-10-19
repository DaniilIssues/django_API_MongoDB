from django.core.management.base import BaseCommand
from mainapp.models import Category, Tag, Image
import json, os

JSON_PATH = 'mainapp/json'


def load_from_json():
    items = []
    with open(os.path.join(JSON_PATH, 'items.json')) as file:
        for item in file:
            data = json.loads(item)
            items.append(data)
    return items


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        Tag.objects.all().delete()
        Image.objects.all().delete()
        categories = []
        tags = []
        items = load_from_json()
        for item in items:
            for tag in item["tags"]:
                if tag not in tags:
                    tags.append(tag)
            cat = item['category'].strip()
            if cat not in categories:
                categories.append(cat)

        for category in categories:
            new_category = Category(name=category)
            new_category.save()
        for tag in tags:
            new_tag = Tag(name=tag)
            new_tag.save()

        for pk, image in enumerate(items):
            tagers = image['tags']
            _source = image['source']
            _author = image['author']
            err = 'Лицензия'
            if err in _author:
                _author = 'null'
            _license = image['license']
            _size = image['size']
            path = [i['path'].strip('full/') for i in image['pic_result']]
            category_name = image['category'].strip()
            category = Category.objects.get(name=category_name)
            new_image = Image(category=category, source=_source, size=_size, author=_author, license=_license,
                              pic_original=f"orig/{path[0]}", pic_min =f"min/{path[0]}")
            new_image.save()
            new = Image.objects.get(pk=pk+1)
            for tag in tagers:
                new_t = Tag.objects.get(name=tag)
                new.tags.add(new_t)

