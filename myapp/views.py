from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from myapp.forms import CustomUserCreationForm, CustomUserChangeForm


# Create your views here.

@login_required
def vista_restringida(request):
    # Tu lógica para la vista restringida aquí
    return render(request, 'vista_restringida.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirige a la página de inicio o a donde desees
            return redirect('home')
        else:
            # Manejo de errores, por ejemplo, mostrar un mensaje de error
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    else:
        return render(request, 'login.html')
    


@login_required
def create_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la página de inicio
    else:
        form = CustomUserCreationForm()
    return render(request, 'create_user.html', {'form': form})

@login_required
def edit_user(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la página de inicio
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'edit_user.html', {'form': form})

@login_required
def delete_user(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('home')  # Redirige a la página de inicio
    return render(request, 'delete_user.html')

def index(request):
    return render(request, 'principal.html')

def login(request):
    return render(request, 'Login.html')

def juego5dos(request):
    return render(request, 'juego5dos.html')

def juego5(request):
    return render(request, 'juego5.html')

def juego4dos(request):
    return render(request, 'juego4dos.html')

def juego4(request):
    return render(request, 'juego4.html')

def juego3dos(request):
    return render(request, 'juego3dos.html')

def juego3(request):
    return render(request, 'juego3.html')

def juego2dos(request):
    return render(request, 'juego2dos.html')

def juego2(request):
    return render(request, 'juego2.html')

def juego1dos(request):
    return render(request, 'juego1dos.html')

def juego1(request):
    return render(request, 'juego1.html')

def form(request):
    return render(request, 'Form.html')

def categoria5(request):
    return render(request, 'Categoria5.html')

def categoria4(request):
    return render(request, 'Categoria4.html')

def categoria3(request):
    return render(request, 'Categoria3.html')

def categoria2(request):
    return render(request, 'Categoria2.html')

def categoria1(request):
    return render(request, 'Categoria1.html')

def carrito(request):
    return render(request, 'carrito.html')
def principal(request):
    return render (request, 'principal.html')