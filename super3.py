from urllib2 import Request, urlopen

values = """
  {
    "ID_SACADO_SAC": "105",
    "ST_NOME_SAC": "Hugo Francisco da Silva",
    "ST_NOMEREF_SAC": "Hugo Francisco da Silva",
    "ST_DIAVENCIMENTO_SAC": "10",
    "ST_TELEFONE_SAC": "9225582486"
  }
"""

headers = {
  'Content-Type': 'application/json',
  'app_token': '3QjxUSc8jWQ8',
  'access_token': 'CXHofZ2YzE2M'
}
request = Request('https://api.superlogica.net/v2/financeiro/clientes', data=values, headers=headers)
request.get_method = lambda: 'PUT'

response_body = urlopen(request).read()
print response_body