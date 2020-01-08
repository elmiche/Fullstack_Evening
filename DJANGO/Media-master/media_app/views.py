from django.shortcuts import render, redirect
from .models import MyModel

def index(request):
        images = MyModel.objects.all()
        context = {

            'images' : images
        }
        return render(request, 'pages/index.html', context)

def image_upload(request):
    if request.method == 'POST':
        image_file = request.FILES.get('image_file')
        upload = MyModel(my_image = image_file)
        upload.save()
        image_url = upload.my_image.url
        return redirect('index')
        
    else:
        images = MyModel.objects.all()
        context = {

            'images' : images
        }
        return render(request, 'pages/upload.html', context)