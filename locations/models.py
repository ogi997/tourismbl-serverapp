from django.contrib.gis.db import models
from choices.models import Visibility, Categories
from users.models import User


class Location(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/ImageLocations")
    category = models.CharField(choices=Categories.choices, max_length=100)
    visibility = models.CharField(choices=Visibility.choices, max_length=100)
    geometry = models.PointField()
    active = models.BooleanField(default=False)

    last_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


