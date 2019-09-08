from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Image(models.Model):
    """
    A Image model. Has a custom save() function, which automatically
    assigns the same value to title and slug. Users can share and like
    images. Images are stored in a folder 'images/year/month/day'.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created',
                             on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)

    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d')

    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)

    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='images_liked')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Image, self).save(*args, **kwargs)
