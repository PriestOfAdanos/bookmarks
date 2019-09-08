from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageUploadForm


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request,'Dodano obraz')
            return redirect(new_item.get_absolute_url())
        messages.error(request, 'Coś poszło nie tak, sprawdź czy podawane przez ciebię dane są poprawne')
    form = ImageUploadForm(request.GET)
    return render(request, 'images/image/create.html', {'section': 'images', 'form': form})
