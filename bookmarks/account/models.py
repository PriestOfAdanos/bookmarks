from django.conf import settings
from django.db import models


class Profile(models.Model):
    """
    Class conected to user model through O_to_O field.
    Allows to store more data and add functionalies without modyfing default user model
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.user.username
