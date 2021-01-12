#Importamos las librerias que necesitamos

import requests
import json

#Les asignamos la url donde tiene que consutlar la ip

url='http://ip-api.com/json/'

#Le damos los parametros que queremos consultar y copi

parametros='city,country,countryCode,isp,org,regionName,lat,lon,timezone,zip'
data={'fields':parametros}

#Definimos la funcion ip_scrap

def ip_scrap(ip=''):
    res=requests.get(url+ip, data=data)
    apires=json.loads(res.content)
    return apires
if __name__ == '__main__':
    ip=input('Ingrese la dirección IP: ')

#Llamamos la funcion ip_scrap y mostramos resultados

par=parametros.split(',')
for x in par:
    print(x.upper(), ':')
    print(ip_scrap(ip)[x])
    