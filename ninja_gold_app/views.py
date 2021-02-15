from django.shortcuts import redirect, render

# python manage.py

def index(request):
    return render(request, 'index.html')


def process_money(request):

    return redirect('/')
