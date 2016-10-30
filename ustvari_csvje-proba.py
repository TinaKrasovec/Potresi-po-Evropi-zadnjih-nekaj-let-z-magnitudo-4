import re
import orodja


def izloci_podatke_potresov(strani):
    regex_potresa = re.compile(
        r'<td class=\".*?>(?P<leto>\d{4})-(?P<mesec>\d{2})-(?P<dan>\d{2}).*?(?P<ura>\d{2}:\d{2}:\d{2})\.\d{1,2}<'
        r'<.*? class=\"tabev\d\">(?P<geo_sirina>\d{2}\.\d{2})&nbsp;<\/td>'
        r'<td class=\"tabev\d\">(?P<geo_dolzina>\d{2}\.\d{2})&nbsp;<\/td>'
        r'<td class=\"tabev\d\">(?P<globina>\d{1,3})<\/td>'
        r'<td class=\"tabev\d\">(?P<magnituda>\d\.\d)<\/td><td id=\".*?\" class=\"tb_region\" >&#160;(?P<drzava>.*?)<\/td>'
        , flags=re.DOTALL)
    
def pocisti_potres(potres):
    podatki = potres.groupdict()
    podatki['leto'] = int(podatki['leto'])
    podatki['mesec'] = int(podatki['mesec'])
    podatki['dan'] = int(podatki['dan'])
    podatki['drzava'] = podatki['drzava'].strip()
    podatki['geo_sirina'] = float(podatki['geo_sirina'])
    podatki['geo_dolzina'] = float(podatki['geo_dolzina'])
    podatki['globina'] = int(podatki['globina'])
    podatki['magnituda'] = float(podatki['magnituda'])
    return podatki


def izloci_podatke_potresov(imenik):
    potresi = []
    for html_datoteka in orodja.datoteke(imenik):
        for potres in re.finditer(regex_potresa, orodja.vsebina_datoteke(html_datoteka)):
            potresi.append(pocisti_potres(potres))
    return potresi


potresi = izloci_podatke_potresov('../../programiranje/projekt/')
orodja.zapisi_tabelo(potresi, ['leto', 'mesec', 'dan', 'drzava', 'geo_sirina', 'geo_dolzina', 'globina', 'magnituda'], 'potresi.csv')

