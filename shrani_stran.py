import requests
import orodja


for stran in range (1,62):
    osnovni_naslov = 'http://www.emsc-csem.org/Earthquake/europe/M4/'
    parametri = 'view='
    naslov = '{}?{}{}'.format(osnovni_naslov, parametri, stran)
    datoteka = 'strani/{:02}.html'.format(stran)
    orodja.shrani(naslov, datoteka)
    print(stran)
