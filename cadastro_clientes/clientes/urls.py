from django.urls import path
from .views import listar_clientes, criar_cliente, editar_cliente, excluir_cliente, buscar_cliente

urlpatterns = [
    path('', listar_clientes, name='listar_clientes'),
    path('novo/', criar_cliente, name='criar_cliente'),
    path('editar/<int:id>/', editar_cliente, name='editar_cliente'),
    path('excluir/<int:id>/', excluir_cliente, name='excluir_cliente'),
    path('buscar/', buscar_cliente, name='buscar_cliente'),
]
