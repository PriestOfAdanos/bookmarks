from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageUploadForm
from django.shortcuts import get_object_or_404
from .models import Image
from django.http import JsonResponse
from django.views.decorators.http import require_POST


@login_required
@require_POST
def image_like(request):
    image_pk = request.POST.get('pk')
    action = request.POST.get('action')
    if image_pk and action:
        try:
            image = Image.objects.get(pk=image_pk)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            pass
    return JsonResponse({'status': 'ok'})


def image_detail(request, pk, slug):
    image = get_object_or_404(Image, pk=pk, slug=slug)
    return render(request, 'images/image/detail.html', {'section': 'images', 'image': image})


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
