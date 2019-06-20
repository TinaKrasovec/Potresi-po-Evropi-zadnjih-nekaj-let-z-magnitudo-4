# Potresi po Evropi zadnjih nekaj let z magnitudo 4+

Ta repozitorij vsebuje projekt pri Programiranju 1 - zajem in analiza podakov.

Podatke sem zajela s spletne strani [emsc-csem.org](http://www.emsc-csem.org/Earthquake/europe/M4/).  
Za potrese sem izbrala tiste, ki so imeli magnitudo večjo od 4 in so se zgodili v obdobju od 7. 1. 2013 do 1. 11. 2016. Zanje sem pridobila podatke za:  
- leto, mesec in dan potresa,  
- uro,  
- geografsko širino in dolžino,  
- globino,  
- magnitudo in  
- državo

## Analizirala bom

Kateri potres je bil najmočnejši,  
v katerem letu je bilo največje število potresov,  
kateri potres je bil najmočnejši v letu, ko je bilo največ potresov,  
v katerem mesecu je bilo največ potresov,  
kateri potres je bil najmočnejši v mesecu, ko jih je bilo največ,  
v kateri državi je bilo največ potresov,  
kje so v povprečju najmočnejši potresi,  
kje je povprečna globina izvora potresa največja in  
ali lahko vidimo kje je največ potresov

## Rezultat

Projekt se nahaja v datoteki Projekt.ipynb.  

## Predpriprava  

Najprej s pomočjo datoteke shrani_stran-popravljena.py spletne strani shranimo v mapo, nato s pomočjo datoteke csv-koncna.py  pretvorimo podatke v tabelo potresi.csv.  
Ostale pythonove datoteke nam pomagajo priti do želene csv datoteke. To datoteko uporabljam pri analizi. Naj omenim še, da orodja.py je datoteka, ki jo je sestavil prof. Pretnar in je v pomoč za končan projekt, ki se nahaja v datoteki Projekt.ipynb.

csv  
Datoteke csv-group.py, csv-groupdict.py in csv-koncna.py so v pomoč za pretvorbo podatkov v tablo (potresi.csv). V teh treh omenjenih datotekah poimenujemo skupine zajetih podatkov. Torej id, leto, mesec, dan in uro potresa ter v kateri državi se je potres zgodil z globino in magnitudo. Naštete podatke izločimo s pomočjo regularnih izrazov iz html strani. Nato podatke še počistimo, da dobimo želene lastnosti in jih s pomočjo csv-koncna.py oblikujemo v csv datoteko (potresi.csv).


