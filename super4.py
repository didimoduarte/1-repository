from urllib2 import Request, urlopen
import json

headers = {
  'Content-Type': 'application/json',
  'app_token': '3QjxUSc8jWQ8',
  'access_token': 'CXHofZ2YzE2M'
}

a = 782
request = Request('https://api.superlogica.net/v2/financeiro/notafiscal/nfeespelhopdf?ID_IMPRESSORA_IMPR=pdf&ID_NOTA_NOT=782&FL_TIPO_NOT=1', headers=headers)
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

