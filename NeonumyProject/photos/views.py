from django.shortcuts import render,get_object_or_404, redirect
from django.http import JsonResponse
from .models import Photo
from .forms import ImageForm
import os

# Create your views here.

def list_photo(request):
    images = Photo.objects.all()
    return  render(request,'photos/photo_list.html',{'images': images})

def image_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'photos/photo_upload.html', {'form': form})

def image_detail(request, pk):
    image = get_object_or_404(Photo, pk=pk)
    return render(request, 'photos/photo_detail.html', {'image': image})

def image_delete(request, pk):
    image = get_object_or_404(Photo, pk=pk)
      # Get the file path
    image_path = image.image.path  

    # Delete the image file from the folder if it exists
    if os.path.isfile(image_path):
        os.remove(image_path)
    image.delete()
    return redirect('image_list')