from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, null=False)
    price = models.PositiveIntegerField()
    image = models.URLField(max_length=300)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=150, unique=True)
