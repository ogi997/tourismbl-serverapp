from django.db import models


class Visibility(models.TextChoices):
    PUBLIC = ("PUBLIC", "Public")
    ONLY_ME = ("ONLY_ME", "Only me")
    LOGGED_USER = ("LOGGED_USER", "Logged user")


class Categories(models.TextChoices):
    ALL = ("ALL", "All")
    SPORT = ("SPORT", "Sport")
    CULTURE = ("CULTURE", "Culture")
    HISTORY = ("HISTORY", "History")
    FOOD_AND_DRINK = ("FOOD_AND_DRINK", "Food and drink")
    OTHER = ("OTHER", "Other")
