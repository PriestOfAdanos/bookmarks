from django import forms
from .models import Image
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify
from django.utils.cache import iri_to_uri


class ImageUploadForm(forms.ModelForm):
    """
    Image upload form, clean_url makes sure that image passed is in
    jpg or jpeg format, custom save()
    """
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('Link prowadzi do obrazu w nieobsługiwanym formacie')
        return url

    def save(self, commit=True, force_insert=False, force_update=False):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        image_extension = image_url.rsplit('.', 1)[1].lower()

        image_name = "{}.{}".format(slugify(image.title), image_extension)
        # making sure iri doesn't raise error

        response = request.urlopen(iri_to_uri(image_url))
        image.image.save(image_name, ContentFile(response.read()), save=False)

        if commit:
            image.save()
        return image


