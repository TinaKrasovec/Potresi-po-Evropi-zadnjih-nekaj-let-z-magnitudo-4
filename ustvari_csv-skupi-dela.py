import re
import orodja


def pocisti_potres(potres):
    podatki = potres.groupdict()
    podatki['id'] = int(podatki['id'])
    podatki['leto'] = int(podatki['leto'])
    podatki['mesec'] = int(podatki['mesec'])
    podatki['dan'] = int(podatki['dan'])
    podatki['drzava'] = podatki['drzava'].strip()
    podatki['ura'] = podatki['ura'].strip()
    podatki['sirina'] = float(podatki['sirina'])
    podatki['dolzina'] = float(podatki['dolzina'])
    podatki['globina'] = int(podatki['globina'])
    podatki['magnituda'] = float(podatki['magnituda'])
    return podatki


def izloci_podatke_potresov(potres):
    regex_potresa = re.compile( 
        r'<a href=".+?\.php\?id=(?P<id>\d{6})">(?P<leto>\d{4})-(?P<mesec>\d{2})-(?P<dan>\d{2}).+?(?P<ura>\d{2}:\d{2}:\d{1,2})\.\d</a>.+?'
        r'<td class="tabev1">(?P<sirina>\d{1,2}\.\d{1,2})&nbsp;</td><td class="tabev2">[NS].+?'
        r'<td class="tabev1">(?P<dolzina>\d{1,2}\.\d{1,2})&nbsp;</td><td class="tabev2">[EW].+?'
        r'<td class=\"tabev\d\">(?P<globina>\d{1,3})<\/td>.+?'
        r'<td class=\"tabev\d\">(?P<magnituda>\d\.\d)<\/td>.+?'
        r'<td id=\".*?\" class=\"tb_region\" >&#160;(?P<drzava>.+?)<\/td>'
        , flags=re.DOTALL)
    potresi = []
    for html_datoteka in orodja.datoteke('strani/'):
        for potres in re.finditer(regex_potresa, orodja.vsebina_datoteke(html_datoteka)):
            potresi.append(pocisti_potres(potres))
            #print(potres.group('id'), potres.group('sirina'), potres.group('magnituda'))
    return potresi

#izloci_podatke_potresov()
potresi = izloci_podatke_potresov('../../projectT/')
orodja.zapisi_tabelo(potresi, ['id', 'leto', 'mesec', 'dan', 'ura', 'drzava', 'sirina', 'dolzina', 'globina', 'magnituda'], 'potresi.csv')
