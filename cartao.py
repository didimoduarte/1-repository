# -*- coding: UTF-8 -*-
from urllib2 import Request, urlopen
import urllib2
import json


def API_PagamentoCartao(form, finaceiro_id):

    request_headers = {
        'Content-Type': 'application/json', 'app_token': '3QjxUSc8jWQ8', 'access_token': 'CXHofZ2YzE2M'
    }

    url = 'https://api.superlogica.net/v2/financeiro/clientes/formadepagamento?ID_SACADO_SAC'
    new_url = "{}={}".format(url, finaceiro_id)
    new_url1 = "{}&{}".format(new_url, 'FL_PAGAMENTOPREF_SAC=3')
    new_url2 = "{}&{}".format(new_url1, 'ST_CARTAOBANDEIRA_SAC')
    new_url3 = "{}={}".format(new_url2, form.cleaned_data.get('bandeira'))
    new_url4 = "{}&{}".format(new_url3, 'ST_CARTAO_SAC')
    new_url5 = "{}={}".format(new_url4, form.cleaned_data.get('num_cartao'))
    new_url6 = "{}&{}".format(new_url5, 'ST_MESVALIDADE_SAC')
    new_url7 = "{}={}".format(new_url6, form.cleaned_data.get('mes_validade'))
    new_url8 = "{}&{}".format(new_url7, 'ST_ANOVALIDADE_SAC')
    new_url9 = "{}={}".format(new_url8, form.cleaned_data.get('ano_valdiade'))
    new_url10 = "{}&{}".format(new_url9, 'ST_SEGURANCACARTAO_SAC')
    new_url11 = "{}={}".format(new_url10, form.cleaned_data.get('cod_seg'))
    new_url12 = "{}&{}".format(new_url11, 'ST_NOMECARTAO_SAC')
    final = "{}={}".format(new_url12, form.cleaned_data.get('nome'))



    request = urllib2.Request(final, headers=request_headers)
    request.get_method = lambda: 'PUT'
    response = urllib2.urlopen(request)

    string = response.read().decode('utf-8')
    json_obj = json.loads(string)

    return json_obj


# finaceiro_id = 105

# retrono = API_PagamentoBoleto(finaceiro_id)
# print retrono[0]['status']


class cobrancas(object):
    'Clase para montar as cobranças do usuários'

    def __init__(self, dict):
        self.id = dict['id_sacado_sac']
        self.nome_fantasia = dict['st_nomeref_sac']
        self.razao_social = dict['st_nome_sac']
        self.numero_cartao = dict['nm_cartao_sac']
        self.telefone = dict['st_telefone_sac']
        self.email = dict['st_email_sac']
        self.cep = dict['st_cep_sac']
        # Padrão é 0(boleto). Caso seja cartão mudar p/ 3
        self.forma_pagamento = dict['fl_pagamentopref_sac']
        # 1 para Pessoa Jurídica e '' para Pessoa Física
        self.tipo_cadastro = dict['fl_pessoajuridica_sac']
        self.cnpj = dict['st_cgc_sac']
        self.bandeira_cartao = dict['st_cartaobandeira_sac']
        # ID utilizado para gerar o boleto
        self.id_boleto = dict['id_recebimento_recb']
        # Data de vencimento do boleto
        self.data_vencimento = dict['dt_vencimento_recb']
        # Data que foi creditado o valor em conta
        self.data_recebimento = dict['dt_recebimento_recb']
        # 0 = boleto em aberto, 1 = pagamento realizado
        self.status_pagamento = dict['fl_status_recb']
        self.valor_pago = dict['vl_total_recb']  # Valor efetivamente pago
        # Valor efetivo da recorrencia
        self.valor_recorrencia = dict['vl_emitido_recb']
        self.data_geracao = dict['dt_geracao_recb']
        # Data que a cobrança foi paga
        self.data_pagamento = dict['dt_liquidacao_recb']
        self.numero_nota = dict['st_nf_recb']  # Número da nota fiscal
        # Forma de pagamento por extenso
        self.forma_pagamento = dict['ar_nomeformas_calc']
        self.link_2via = dict['link_2via']  # Link p/ 2 via


# lista = retorno['id_nota_not']
# for item in lista:st_documentoex_recb
# LinkEspelhoNotaFiscalprint retorno

# for item in retorno['nota']:
# print item

# print type(retorno)
# print len(response)
# print request


def LinkEspelhoNotaFiscal(id_nota):
    headers = {
        'Content-Type': 'application/json',
        'app_token': '3QjxUSc8jWQ8',
        'access_token': 'CXHofZ2YzE2M'
    }

    url = 'https://api.superlogica.net/v2/financeiro/notafiscal/nfeespelhopdf?ID_IMPRESSORA_IMPR=pdf&ID_NOTA_NOT'
    new_url = "{}={}".format(url, id_nota)
    u1 = "{}&{}".format(new_url, 'FL_TIPO_NOT=1')

    request = Request(u1, headers=headers)
    request.get_method = lambda: 'POST'

    response_body = json.loads(urlopen(request).read().decode('utf-8'))
    print response_body["id_impressao"]

    url = 'https://api.superlogica.net/v2/financeiro/impressoes?FL_COMPARTILHAR=1&ID_IMPRESSAO_FIMP'
    new_url = "{}={}".format(url, response_body["id_impressao"])

    reques_link = Request(new_url, headers=headers)
    reques_link.get_method = lambda: 'PUT'
    response_link = json.loads(urlopen(reques_link).read().decode('utf-8'))
    link = response_link[0]['data']['link_externo']
    print link
    return link


# LinkEspelhoNotaFiscal(782)
