from django.urls import path
from . import views

app_name = 'loja'

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('comprar/<int:produto_id>/', views.comprar, name='comprar'),
    path('processar-pedido/', views.processar_pedido, name='processar_pedido'),
    path('contato/', views.contato, name='contato'),
]
