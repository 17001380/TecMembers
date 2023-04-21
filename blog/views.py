from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import TecMembers
from itertools import chain
from django.db.models import Q
# Create your views here.



def home(request):
    Q1 = TecMembers.objects.all()
    Context = {
        'posts': Q1,
        'lables':{
            'Soluciones Tecnologicas': {'Fintech','Software empresaliral','Software a la medida','Robotica','Cyber Seguridad','Electronica','Data Center','Bio-Tech','Medios digitales','Venture Capital','Equipos de computo','Servicios de internet','Otras tecnologias'},
            'Otros Servicios': {'Servicios a ecosistema','Comercio'},
            
        }
    }

    return render(request, 'blog/home.html',Context)

def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})

def search(request):
    if request.method == "POST":
        Busqueda = request.POST['Busqueda']
        if "," in Busqueda:
             bus1 = Busqueda.split(",")
             queryset = TecMembers.objects.filter(Q(Clas1__contains=bus1[1]))
             
        else:
            queryset = TecMembers.objects.filter(
                Q(Clas1__contains=Busqueda) | 
                Q(Sub_Clas1__contains=Busqueda) | 
                Q(Sub_Clas2__contains=Busqueda)| 
                Q(Sub_Clas3__contains=Busqueda)| 
                Q(Sub_Clas4__contains=Busqueda)| 
                Q(Specific__contains=Busqueda)| 
                Q(Co_Name__contains=Busqueda)
            )

        Context = {
            
            'posts': queryset,
            'lables':{
            'Soluciones Tecnologicas': {'Fintech','Software empresaliral','Software a la medida','Robotica','Cyber Seguridad','Electronica','Data Center','Bio-Tech','Medios digitales','Venture Capital','Equipos de computo','Servicios de internet','Otras tecnologias'},
            'Otros Servicios': {'Servicios a ecosistema','Comercio'},
            
        }
        }
        
        return render(request, 'blog/Search.html',Context)
    else:
        Context = {
            'posts': TecMembers.objects.all()
        }
        return render(request, 'blog/Search.html',{'Busqueda':Busqueda})