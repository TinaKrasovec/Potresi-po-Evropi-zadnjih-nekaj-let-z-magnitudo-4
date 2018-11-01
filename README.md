# Potresi-po-Evropi-zadnjih-nekaj-let-z-magnitudo-4+

Ta repozitorij vsebuje projekt pri Programiranju 1 - zajem in analiza podakov.

Podatke sem zajela s spletne strani http://www.emsc-csem.org/Earthquake/europe/M4/.  
Za potrese od 7. 1. 2013 do 1. 11. 2016 sem pridobila podatke za:  
leto, mesec in dan potresa,  
uro,  
geografsko širino in dolžino,  
globino,  
magnitudo in  
državo

##Analizirala bom / hipoteze  

Kateri je bil najmočnejši potres,  
v katerem letu je bilo največ potresov,  
kateri potres je bil najmočnejši v letu, ko je bilo največ potresov,  
v katerem mesecu je bilo največ potresov,  
kateri potres je bil najmočnejši v mesecu, ko jih je bilo največ,  
v kateri državi je bilo največ potresov,  
kje so v povprečju najmočnejši potresi,  
kje je povprečna globina izvora potresa največja in  
ali lahko vidimo kje je največ potresov

##Predpriprava  

Najprej s pomočjo datoteke shrani_stran-popravljena.py spletne strani shranimo v mapo, nato s pomočjo datoteke csv-koncna.py  pretvorimo podatke v tabelo potresi.csv.  
Ostale pythonove datoteke nam pomagajo priti do želene csv datoteke.

csv  
Datoteke csv-group.py, csv-groupdict.py in csv-koncna.py so v pomoč za pretvorbo podatkov v tablo (potresi.csv). V teh treh omenjenih datotekah poimenujemo skupine zajetih podatkov. Torej id, leto, mesec, dan in uro potresa ter v kateri državi se je potres zgodil z globino in magnitudo. Naštete podatke izločimo s pomočjo regularnih izrazov iz html strani. Nato podatke še počistimo, da dobimo želene lastnosti in jih s pomočjo csv-koncna.py oblikujemo v csv datoteko (potresi.csv).

##Rezultati  

Projekt se nahaja v datoteki Projekt.ipynb.  
Ostale datoteke pa so namenjene zapisu osnovnih funkcij.
