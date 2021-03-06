import re
import orodja

def izloci_podatke_potresov():
    regex_potresa = re.compile( 
        r'<a href=".+?\.php\?id=(?P<id>\d{6})">(?P<leto>\d{4})-(?P<mesec>\d{2})-(?P<dan>\d{2}).+?(?P<ura>\d{2}:\d{2}:\d{1,2})\.\d</a>.+?'
        r'<td class="tabev1">(?P<sirina>\d{1,2}\.\d{1,2})&nbsp;</td><td class="tabev2">[NS].+?'
        r'<td class="tabev1">(?P<dolzina>\d{1,2}\.\d{1,2})&nbsp;</td><td class="tabev2">[EW].+?'
        r'<td class=\"tabev\d\">(?P<globina>\d{1,3})<\/td>.+?'
        r'<td class=\"tabev\d\">(?P<magnituda>\d\.\d)<\/td>.?'
        r'<td id="reg\d+" class="tb_region" >&#160;(?P<drzava>.+?)<\/td>'
        , flags=re.DOTALL)
    for html_datoteka in orodja.datoteke('strani/'):
        for potres in re.finditer(regex_potresa, orodja.vsebina_datoteke(html_datoteka)):
            print(potres.group('magnituda'), potres.group('drzava'))

izloci_podatke_potresov()
