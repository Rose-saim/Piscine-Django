from django.shortcuts import render

def django_info(request):
    return render(request, 'ex01/django.html')

def display_process(request):
    return render(request, 'ex01/affichage.html')

def template_engine(request):
    return render(request, 'ex01/templates.html')
