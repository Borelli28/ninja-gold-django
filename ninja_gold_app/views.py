from django.shortcuts import render

#python manage.py

def index(request):
    return render(request, 'index.html')
