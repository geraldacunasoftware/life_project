from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .models import Category, Service
from life_project import settings
from django.core.mail import send_mail

def envio(request):
    if request.method == 'POST':
        subject = request.POST['asunto']
        message = request.POST['message'] + ' ' + request.POST['email']
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['cotizaciones@lifeprintcr.com']
        send_mail(subject, message, email_from, recipient_list)
        print('enviado')
        return redirect('index')  # Cambié render por redirect para redirigir a la página de inicio

def index(request):
    categorys = Category.objects.all()
    return render(request, 'index.html', {'categorys': categorys, 'active_page': 'index'})

def service(request, pk):
    category_ = Category.objects.get(pk=pk)
    # Aplico un filtro en el atributo categoria que me haga una lista con los servicios de la misma categoria
    servicios_category = Service.objects.filter(category=category_)
    print('Servicios de la categoria ')
    print(servicios_category)
    return render(request, 'service.html', {'services': servicios_category, 'active_page': 'service'})
