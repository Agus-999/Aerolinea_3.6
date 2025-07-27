from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistroForm
from django.contrib.auth import get_user_model

User = get_user_model()

def inicio(request):
    return render(request, 'inicio.html')

def vista_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Asignar rol "admin" si es superusuario
            if user.is_superuser and user.rol != 'admin':
                user.rol = 'admin'
                user.save()

            login(request, user)
            return redirect('inicio')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'assets/login.html')

def vista_registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.rol = 'cliente'  # Por defecto
            usuario.save()
            messages.success(request, 'Registro exitoso. Ahora podés iniciar sesión.')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'assets/register.html', {'form': form})

def vista_logout(request):
    logout(request)
    return redirect('login')
