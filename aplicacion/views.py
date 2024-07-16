from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView
from .forms import RegistroForm
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
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # <- Usa el alias aquí
            return redirect('home')  # Redirige a la página principal después del registro
    else:
        form = RegistroForm()
    return render(request, 'aplicacion/registro.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'aplicacion/login.html'