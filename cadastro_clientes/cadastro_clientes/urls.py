from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # Import necessário para o redirecionamento

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('', lambda request: redirect('/clientes/', permanent=True)),  # Redireciona a URL raiz para /clientes/
]
