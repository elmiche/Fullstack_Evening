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
        image_file = request.FILES.get('image_file') #gets file from the form under the same name 'image_file'
        upload = MyModel(my_image = image_file) #save the file to the variable 
        upload.save()
        image_url = upload.my_image.url #saving the file you got to the model 
        return redirect('index')
        
    else:
        images = MyModel.objects.all()
        context = {

            'images' : images
        }
        return render(request, 'pages/upload.html', context)