from django.db import models
from Items.models import Items
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    item = models.ForeignKey(Items, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, blank=True)

    def __str__(self):
        return "Cart: " + self.item.title