'''
Created on 5 jul. 2022

@author: xavier.ruiz
'''
import requests
import json
from model.cliente import cliente
from util.leer_txt import leer_txt
archivo=open("Clientes.txt","r")
cliente1=cliente("","","","","")
cliente2=cliente("","","","","")
leer=leer_txt()
cliente1,cliente2=leer.leer(archivo)
cliente1.__str__()
cliente2.__str__()
auth_data = {'nombre': cliente1.nombre, 'apellido': cliente1.apellido,'pais':cliente1.pais,'idioma':cliente1.idioma,'nombreAeropuerto':cliente1.nombreAeropuerto}
auth_data2= {'nombre': cliente2.nombre, 'apellido': cliente2.apellido,'pais':cliente2.pais,'idioma':cliente2.idioma,'nombreAeropuerto':cliente2.nombreAeropuerto}
print(json.dumps(auth_data))
resp = requests.post('http://localhost:7070/examen/apiv1/clientes/add', json=auth_data)
resp2 = requests.post('http://localhost:7070/examen/apiv1/clientes/add', json=auth_data2)
