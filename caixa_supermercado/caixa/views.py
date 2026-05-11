from django.shortcuts import render
from .troco import alg_troco

def index(request):
    return render(request, 'caixa/index.html')

def selecao(request):
    return render(request, 'caixa/selecao.html')

def pagamento(request):
    return render(request, 'caixa/pagamento.html')

def confirmacao(request):
    return render(request, 'caixa/confirmacao.html')
