from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import TecMembers
# Create your views here.



def home(request):
    Context = {
        'posts': TecMembers.objects.all()
    }
    return render(request, 'blog/home.html',Context)

def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})

def search(request):
    if request.method == "POST":
        Busqueda = request.POST['Busqueda']
        Context = {
            'posts': TecMembers.objects.filter(Clas1__contains=Busqueda)
        }
        
        return render(request, 'blog/Search.html',Context)
    else:
        Context = {
            'posts': TecMembers.objects.all()
        }
        return render(request, 'blog/Search.html',{'Busqueda':Busqueda})