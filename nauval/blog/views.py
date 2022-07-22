from django.shortcuts import render

# Create your views here.

def index(request):
    context ={
        'judul':'BLOG'
    }
    return render(request,'blog/index.html',context)