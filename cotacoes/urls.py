from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pdf/', views.gerar_pdf, name='gerar_pdf'),
]
