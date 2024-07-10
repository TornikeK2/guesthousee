from django.db import models


class ContactInfo(models.Model):
    email = models.EmailField(max_length=254)
    number = models.IntegerField()
    message = models.TextField()