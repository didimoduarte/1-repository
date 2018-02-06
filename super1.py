# -*- coding: UTF-8 -*-
import urllib2
import urllib
import json

def teste(id_superlogica):

	request_headers = {
	'Content-Type': 'application/json', 'app_token': '3QjxUSc8jWQ8', 'access_token': 'CXHofZ2YzE2M'
	}


	url = 'https://api.superlogica.net/v2/financeiro/cobranca?doClienteComId'
	new_url = "{}={}".format(url, id_superlogica)
	final = "{}&{}".format(new_url, 'status=todos')
	request = urllib2.Request(final, headers=request_headers)


	#response = json.loads(urllib2.urlopen(request).read())
	request.get_method = lambda: 'GET'
	response = urllib2.urlopen(request)

	string = response.read().decode('utf-8')
	json_obj = json.loads(string)

	return json_obj
	#print retorno

a = teste(94)
print len(a)
