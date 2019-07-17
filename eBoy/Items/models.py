from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
from Categories.models import Categories
import json

class ItemsQuerySet(models.QuerySet):
    def serialize(self):
        listValues = list(self.values('id', 'title', 'image', 'price', 'slug', 'date', 'user'))
        return json.dumps(listValues, cls=DjangoJSONEncoder)

class ItemsManager(models.Manager):
    def get_queryset(self):
        return ItemsQuerySet(self.model, using=self.db)

class Items(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    slug = models.CharField(max_length=210, blank=True)
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    objects = ItemsManager()

    def __str__(self):
        return self.title
    
    def serialize(self):
        try:
            image = self.image.url
        except:
            image = ""
        data = {
            'id': self.id,
            'title': self.title,
            'image': image,
            'price': self.price,
            'slug': self.slug,
            'user': self.user.id
        }
        return json.dumps(data, cls=DjangoJSONEncoder)

    class Meta:
        verbose_name_plural = 'Items'