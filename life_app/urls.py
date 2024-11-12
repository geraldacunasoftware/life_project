from django.urls import path
from .views import index,service,envio
app_name = 'life_app'

urlpatterns = [
    path('life_app/<int:pk>',service,name='service'),
]