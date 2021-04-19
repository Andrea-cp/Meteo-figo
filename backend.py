import os
from tkinter import messagebox as mBox
try:
    import requests
except ImportError:
    print('Tentativo di installare il modulo richiesto: requirements')
    os.system('pip install -r requirements.txt')
import yaml
import requests
from xml.dom import minidom

with open('config.yaml', 'r') as ymlconfig:
    config = yaml.load(ymlconfig, Loader=yaml.FullLoader)

api_key = config['API']



class Meteo(object):

    id_citta = ""
    nome = ""
    lon = ""
    lat = ""
    nazione = ""
    temperatura_corrente = ""
    temperatura_massima = ""
    temperatura_minima = ""
    umidita = ""
    ultimo_aggiornamento = ""
    tempo_metereologico = ""
    tempo_metereologico_icon = ""
    errore=1

    def __init__(self):
        pass

    def setta_parametri(self, nome_citta):
        url = api_key % nome_citta
        try:
            xmldata = requests.get(url)
            xdp = minidom.parseString(xmldata.text)

            self.id_citta = xdp.getElementsByTagName("city")[0].getAttribute("id")
            self.nome = xdp.getElementsByTagName("city")[0].getAttribute("name")
            self.lon = xdp.getElementsByTagName("coord")[0].getAttribute("lon")
            self.lat = xdp.getElementsByTagName("coord")[0].getAttribute("lat")
            self.nazione = xdp.getElementsByTagName("city")[0].getElementsByTagName("country")[0].firstChild.nodeValue
            self.temperatura_corrente = format(
                float((xdp.getElementsByTagName("temperature")[0].getAttribute("value"))) - 273.15, '.1f')
            self.temperatura_massima = format(
                float((xdp.getElementsByTagName("temperature")[0].getAttribute("max"))) - 273.15, '.1f')
            self.temperatura_minima = format(
                float((xdp.getElementsByTagName("temperature")[0].getAttribute("min"))) - 273.15, '.1f')
            self.umidita = (xdp.getElementsByTagName("humidity")[0].getAttribute("value")) + (
                xdp.getElementsByTagName("humidity")[0].getAttribute("unit"))
            self.ultimo_aggiornamento = (xdp.getElementsByTagName("lastupdate")[0].getAttribute("value")).replace('T',
                                                                                                                  ' ')
            self.tempo_metereologico = xdp.getElementsByTagName("weather")[0].getAttribute("value")
            self.tempo_metereologico_icon = xdp.getElementsByTagName("weather")[0].getAttribute("icon")
            self.errore = 0

        except:
            self.errore = 1











meteo = Meteo()




