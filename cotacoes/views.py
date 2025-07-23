import requests
from django.shortcuts import render
from .models import Cotacao
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from datetime import datetime

def index(request):
    moedas = {'USD': 'Dólar', 'EUR': 'Euro', 'BTC': 'Bitcoin', 'ETH': 'Ethereum'}
    cotacoes = {}
    erros = []

    # TENTATIVA 1: exchangerate.host
    try:
        r = requests.get('https://api.exchangerate.host/latest?base=BRL')
        data = r.json()

        if 'rates' in data and 'USD' in data['rates'] and 'EUR' in data['rates']:
            cotacoes['USD'] = round(1 / data['rates']['USD'], 2)
            cotacoes['EUR'] = round(1 / data['rates']['EUR'], 2)
        else:
            raise ValueError("Resposta inesperada da API exchangerate.host")

    except Exception as e:
        # TENTATIVA 2: frankfurter.app
        try:
            fallback = requests.get('https://api.frankfurter.app/latest?from=BRL&to=USD,EUR')
            fallback_data = fallback.json()

            if 'rates' in fallback_data and 'USD' in fallback_data['rates'] and 'EUR' in fallback_data['rates']:
                cotacoes['USD'] = round(1 / fallback_data['rates']['USD'], 2)
                cotacoes['EUR'] = round(1 / fallback_data['rates']['EUR'], 2)
            else:
                erros.append('Erro nas duas APIs de moedas tradicionais.')

        except Exception as e2:
            erros.append(f'Erro API reserva (frankfurter): {e2}')

    # COTAÇÕES CRIPTOMOEDAS
    try:
        cripto = requests.get('https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=BRL')
        cripto_data = cripto.json()

        if 'BTC' in cripto_data and 'ETH' in cripto_data:
            cotacoes['BTC'] = cripto_data['BTC']['BRL']
            cotacoes['ETH'] = cripto_data['ETH']['BRL']
        else:
            erros.append('Erro ao acessar criptomoedas.')

    except Exception as e:
        erros.append(f'Erro API Cripto: {e}')

    # SALVAR COTAÇÕES NO BANCO
    for tipo, valor in cotacoes.items():
        Cotacao.objects.create(tipo=tipo, valor=valor)

    context = {
        'cotacoes': cotacoes,
        'data_hora': datetime.now(),
        'moedas': moedas,
        'erros': erros,
    }
    return render(request, 'index.html', context)

def gerar_pdf(request):
    template = get_template('relatorio.html')
    moedas = ['USD', 'EUR', 'BTC', 'ETH']
    registros = Cotacao.objects.filter(tipo__in=moedas).order_by('-data_hora')[:10]
    context = {
        'registros': registros,
        'data_hora_geracao': datetime.now()
    }
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="relatorio.pdf"'
    pisa.CreatePDF(html, dest=response)
    return response


