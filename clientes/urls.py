from django.urls import path
from .views import cadastrar_cliente, listar_clientes


urlpatterns = [
    path('cadastrar/', cadastrar_cliente, name='cadastrar_cliente'),
    path('listar/', listar_clientes, name='listar_clientes'),
]