from django.shortcuts import render

def index(request):
    # Ваш код для головної сторінки
    return render(request, 'index.html')

def about(request):
    # Ваш код для сторінки about.html
    return render(request, 'about.html')

# Create your views here.
