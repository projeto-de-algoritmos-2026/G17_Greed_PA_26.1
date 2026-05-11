from django.shortcuts import render
from .troco import alg_troco, para_centavos
from .models import Produto
from decimal import Decimal
from django.shortcuts import render 
import json

MOEDAS = [
    Decimal('200.00'),
    Decimal('100.00'),
    Decimal('50.00'),
    Decimal('20.00'),
    Decimal('10.00'),
    Decimal('5.00'),  
    Decimal('1.00'),
    Decimal('0.50'),
    Decimal('0.25'),
    Decimal('0.10'),
    Decimal('0.05'),
]


def index(request):
    return render(request, 'caixa/index.html')

def selecao(request):
    produtos = []
    for p in Produto.objects.filter(ativo=True).order_by('id'):
        produtos.append({
            'id': p.id,
            'nome': p.nome,
            'preco_centavos': p.preco,
            'imagem': p.imagem.url if p.imagem else '',
        })

    return render(request, 'caixa/selecao.html', {
        'produtos_data': produtos
    })

def pagamento(request):
    if request.method == 'POST':
        carrinho_json = request.POST.get('carrinho_json', '[]')
        carrinho = json.loads(carrinho_json)
        request.session['carrinho'] = carrinho

    carrinho = request.session.get('carrinho', [])
    total_compra = sum(
        Decimal(str(item['preco_centavos'])) * int(item['quantidade'])
        for item in carrinho
    )

    return render(request, 'caixa/pagamento.html', {
        'total_compra': total_compra
    })

def confirmacao(request):
    carrinho = request.session.get('carrinho', [])
    total_compra = sum(
        Decimal(str(item['preco_centavos'])) * int(item['quantidade'])
        for item in carrinho
    )

    pago = Decimal('0.00')

    if request.method == 'POST':
        pago_json = request.POST.get('pago_json', '[]')
        pagamentos = json.loads(pago_json)

        for item in pagamentos:
            pago += Decimal(str(item['valor'])) * int(item['quantidade'])

    troco = pago - total_compra

    moedas_centavos = [para_centavos(m) for m in MOEDAS]
    troco_itens = []
    mapa_imagens = {
        Decimal('200.00'): 'caixa/img/cedula_200r.png',
        Decimal('100.00'): 'caixa/img/cedula_100r.png',
        Decimal('50.00'): 'caixa/img/cedula_50r.png',
        Decimal('20.00'): 'caixa/img/cedula_20r.png',
        Decimal('10.00'): 'caixa/img/cedula_10r.png',
        Decimal('5.00'): 'caixa/img/cedula_5r.png',
        Decimal('1.00'): 'caixa/img/moeda_1r.png',
        Decimal('0.50'): 'caixa/img/moeda_50c.png',
        Decimal('0.25'): 'caixa/img/moeda_25c.png',
        Decimal('0.10'): 'caixa/img/moeda_10c.png',
        Decimal('0.05'): 'caixa/img/moeda_5c.png',
    }

    if troco > 0:
        troco_centavos = int(troco)  # já está em centavos
        contagem = alg_troco(troco_centavos, moedas_centavos)
        troco_itens = []
        for valor, qtd in zip(MOEDAS, contagem):
            if qtd > 0:
                troco_itens.append({
                    'valor': valor,
                    'qtd': qtd,
                    'imagem': mapa_imagens[valor]
                })  

    return render(request, 'caixa/confirmacao.html', {
        'total_compra': total_compra/100,
        'pago': pago/100,
        'troco': troco/100 if troco > 0 else Decimal('0.00'),
        'troco_itens': troco_itens,
        'carrinho': carrinho,
    })
