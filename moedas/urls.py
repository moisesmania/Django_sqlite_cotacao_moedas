from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cotacoes.urls')),  # ou o nome do seu app
]
