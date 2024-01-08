from django.contrib.gis.db import models
from choices.models import Visibility, Categories
from users.models import User


class LocationUpdateRequest(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/ImageUpdateRequest")
    category = models.CharField(choices=Categories.choices, max_length=100)
    visibility = models.CharField(choices=Visibility.choices, max_length=100)

    last_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    creation_date = models.DateTimeField(auto_now_add=True)
    id_update = models.IntegerField()
