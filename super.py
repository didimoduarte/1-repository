# -*- coding: UTF-8 -*-
from urllib2 import Request, urlopen
import urllib2
import json


request_headers = {
    'Content-Type': 'application/json',
    'app_token': '3QjxUSc8jWQ8',
    'access_token': 'CXHofZ2YzE2M'}


id_superlogica = 85
url = 'https://api.superlogica.net/v2/financeiro/cobranca?doClienteComId'
new_url = "{}={}".format(url, id_superlogica)
final = "{}&{}".format(new_url, 'status=todos')
request = urllib2.Request(final, headers=request_headers)


# response = json.loads(urllib2.urlopen(request).read())
request.get_method = lambda: 'GET'
response = urllib2.urlopen(request)

string = response.read().decode('utf-8')
json_obj = json.loads(string)

# data = response.read()
# print type(json_obj[0])
retorno = json_obj[4]
# print retorno2


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


lista = retorno['id_nota_not']
# for item in lista:st_documentoex_recb
# LinkEspelhoNotaFiscalprint retorno

# for item in retorno['nota']:
# print item

# print type(retorno)
# print len(response)
print type(json_obj)


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


LinkEspelhoNotaFiscal(782)
