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
            'Hardware': {'Hardware','Aeronoautica','Venta de equipo','Servicios a emprendedores ','Desarrollo Enterprise','Telecomunicaciones','Venta de Software','Ciberseguridad','Geolocalizacion','Comercios','Desarrollo Digital'},
            'SaaS': {'Desarrollo Enterprise','Data Analycis','Fintech','Data Base','e-Learning','Venta de Software','Ciberseguridad','Nube','Educativo'},
            'Comercio': {'Comercios','Venta de equipo','Servicios'},
            'Otras Tecnologias': {'Emprendimiento','IT Administrativo','e-Learning','Bio-Tecnologia','Desarrollo Enterprise','Energia','Hardware','Diseño y Prototipado','Venta de equipo','Telecomunicaciones','Servicios a emprendedores','Tecnologia fianciera','Desarrollo Digital','Servicios','Geolocalizacion','Comercios'},
            'Digital media': {'Desarrollo Enterprise','Desarrollo Digital','Mercadeo Digital','Multimedia','Servicios a emprendedores ','e-Learning'},
            'Software empresarial': {'Desarrollo Enterprise','Telecomunicaciones','Desarrollo Digital','Data Analycis','Tecnologia fianciera','Fintech','Venta de Software'},
            'Servicios ecosistema': {'Servicios','Salud','Desarrollo Enterprise','Ciberseguridad','Venta de Software','Nube','Desarrollo Digital'}
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
             queryset = TecMembers.objects.filter(
                Q(Clas1__contains=bus1[0]) & 
                Q(Sub_Clas1__contains=bus1[1])| 
                Q(Sub_Clas2__contains=bus1[1])| 
                Q(Sub_Clas3__contains=bus1[1])| 
                Q(Sub_Clas4__contains=bus1[1])
            )
             
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
            'Hardware': {'Hardware','Aeronoautica','Venta de equipo','Servicios a emprendedores ','Desarrollo Enterprise','Telecomunicaciones','Venta de Software','Ciberseguridad','Geolocalizacion','Comercios','Desarrollo Digital'},
            'SaaS': {'Desarrollo Enterprise','Data Analycis','Fintech','Data Base','e-Learning','Venta de Software','Ciberseguridad','Nube','Educativo'},
            'Comercio': {'Comercios','Venta de equipo','Servicios'},
            'Otras Tecnologias': {'Emprendimiento','IT Administrativo','e-Learning','Bio-Tecnologia','Desarrollo Enterprise','Energia','Hardware','Diseño y Prototipado','Venta de equipo','Telecomunicaciones','Servicios a emprendedores','Tecnologia fianciera','Desarrollo Digital','Servicios','Geolocalizacion','Comercios'},
            'Digital media': {'Desarrollo Enterprise','Desarrollo Digital','Mercadeo Digital','Multimedia','Servicios a emprendedores ','e-Learning'},
            'Software empresarial': {'Desarrollo Enterprise','Telecomunicaciones','Desarrollo Digital','Data Analycis','Tecnologia fianciera','Fintech','Venta de Software'},
            'Servicios ecosistema': {'Servicios','Salud','Desarrollo Enterprise','Ciberseguridad','Venta de Software','Nube','Desarrollo Digital'}
        }
        }
        
        return render(request, 'blog/Search.html',Context)
    else:
        Context = {
            'posts': TecMembers.objects.all()
        }
        return render(request, 'blog/Search.html',{'Busqueda':Busqueda})