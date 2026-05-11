from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('selecao/',  views.selecao,     name='selecao'),

    path('selecao/pagamento/',  views.pagamento, name='pagamento'),

    path('selecao/confirmacao/',  views.confirmacao, name='confirmacao'),
]