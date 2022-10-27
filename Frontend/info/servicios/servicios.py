import requests
import json

class servicios:
    def getServicios():
        return json.loads(requests.get('http://127.0.0.1:5000/consultaDatos').text)

    def creandoServicio(data):
        response=requests.post('http://127.0.0.1:5000/consultaDatos', json=data)
        return json.loads(response.text)
