from django.shortcuts import render
import string
import secrets

#from django.http import HttpResponse

# Create your views here.

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, "home.html")


def password(request):
    length= int(request.GET.get('length'))
    
    letras = string.ascii_lowercase
    letrasm = string.ascii_uppercase
    digitos = string.digits
    especial = string.punctuation
    if request.GET.get('mayusculas'):
        letras = letras + letrasm
    if request.GET.get('digitos'):
        letras = letras + digitos
        
    if request.GET.get('especial'):
        letras = letras + especial

    contra = ""
    for i in range (length):
        contra += "".join(secrets.choice(letras))

    return render(request, "password.html",{'password': contra})

 
