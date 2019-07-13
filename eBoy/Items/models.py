from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from Categories.models import Categories

class Items(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    slug = models.CharField(max_length=210, blank=True)
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Items'