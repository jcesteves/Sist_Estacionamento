from django.urls import path
from .views import home, contato, servicos, sobre, planos

urlpatterns = [
    path('', home, name='website_home'),
    path('servicos', servicos, name='website_servico'),
    path('sobre', sobre, name='website_sobre'),
    path('planos', planos, name='website_planos'),
    path('contato', contato, name='website_contato'),

 ]
