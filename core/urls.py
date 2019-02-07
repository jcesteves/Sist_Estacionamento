from django.urls import path, include
from .views import (home,
                    lista_pessoas,
                    lista_veiculos,
                    lista_movrotativos,
                    lista_mensalistas,
                    lista_movmensalistas,
                    pessoa_nova,
                    veiculo_novo,
                    movrot_novo,
                    mensalista_novo,
                    movmen_novo,
                    pessoa_update,
                    veiculo_update,
                    movrot_update,
                    mensalista_update,
                    movmen_update,
                    pessoa_delete,
                    veiculo_delete,
                    movrot_delete,
                    mensalista_delete,
                    movmen_delete,
                    pdf, relat_csv)

urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas', lista_pessoas, name='core_lista_pessoas'),
    path('pessoa_nova', pessoa_nova, name='lista_pessoa_nova'),
    path('pessoa-update/<int:id>/', pessoa_update, name='core_pessoa_update'),
    path('pessoa-delete/<int:id>/', pessoa_delete, name='core_pessoa_delete'),
    path('veiculos', lista_veiculos, name='core_lista_veiculos'),
    path('veiculo-novo', veiculo_novo, name='core_veiculo_novo'),
    path('veiculo-update/<int:id>/', veiculo_update, name='core_veiculo_update'),
    path('veiculo-delete/<int:id>/', veiculo_delete, name='core_veiculo_delete'),
    path('movrot', lista_movrotativos, name='core_lista_movrot'),
    path('movrot-novo', movrot_novo, name='core_movrot_novo'),
    path('movrot-update/<int:id>/', movrot_update, name='core_movrot_update'),
    path('movrot-delete/<int:id>/', movrot_delete, name='core_movrot_delete'),
    path('mensalista', lista_mensalistas, name='core_lista_mensalistas'),
    path('mensalista-novo', mensalista_novo, name='core_mensalista_novo'),
    path('mensalista-update/<int:id>/', mensalista_update, name='core_mensalista_update'),
    path('mensalista-delete/<int:id>/', mensalista_delete, name='core_mensalista_delete'),
    path('movmen', lista_movmensalistas, name='core_lista_movmensalistas'),
    path('movmen-novo', movmen_novo, name='core_movmen_novo'),
    path('movmen-update/<int:id>/', movmen_update, name='core_movmen_update'),
    path('movmen-delete/<int:id>/', movmen_delete, name='core_movmen_delete'),
    path('relatorio/', pdf.as_view(), name='relatorio_pdf'),
    path('relat_csv/', relat_csv.as_view(), name='relatorio_csv')
]
