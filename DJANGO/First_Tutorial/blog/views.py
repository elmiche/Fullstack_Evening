from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse
# we don't need this anymore, since we're rendered the templates



#dummy data
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content':'First post content',
        'date_posted': 'August 27, 2018',
    },
     {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content':'Second post content',
        'date_posted': 'August 28, 2018',
    }
]
# after we made a database call and we want to display these posts on our blog template

#we then create a dictionary for our post data

def home(request):
    #using key 'posts' insert the value posts (the dictionary uptop)
    context = {
        'posts': posts
    } 
    return render(request, 'blog/home.html', context) #third arguement to render context, so now whatever keyname we use in context ('posts') will give us access to the post data
    #rendering routes to templates

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) #rendering routes to templates
 

