from django.shortcuts import render

# Create your views here.
def addproduc(request):
    return render(request,'aplicacion/addproduc.html')

def adm(request):
    return render(request,'aplicacion/adm.html')

def admpagregar(request):
    return render(request,'aplicacion/admpagregar.html')

def admpedidos(request):
    return render(request,'aplicacion/admpedidos.html')

def Arriendos(request):
    return render(request,'aplicacion/Arriendos.html')

def editarprod(request):
    return render(request,'aplicacion/editarprod.html')

def login(request):
    return render(request,'aplicacion/login.html')

def registro(request):
    return render(request,'aplicacion/registro.html')