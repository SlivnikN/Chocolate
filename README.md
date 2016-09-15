# Chocolate

## Opis projekta
Za projekt sem si izbrala analizo čokoladnih ovitkov, ki sem jih zbrala v preteklih letih. Podatki o čokoladah so:
* proizvajalec,
* zbirka,
* podzbirka,
* ime,
* zaporedna številka,
* barva.

Primer: Pri temni čokoladi Lindt z meto je proizvajalec Lindt & Sprűngli, zbirka Excellence, podzbirka Fin Cœur, ime Mint Intense Dark, zaporedna številka 5, ker je bila 5. po vrsti, od kar sem jih začela zbirati, barva pa Dark (temna čokolada).
Analizirali bomo število čokolad posameznega proizvajalca v zbirki, število čokolad posamezne vrste (bela, mlečna, temna).

## Hipoteze
* Največ čokolad je od proizvajalca Lindt & Sprűngli,
* večina proizvajalcev ima manj kot 5 čokolad,
* barva čokolade se po obdobjih spreminja (obdobje je 50 čokolad),
* največ je mlečnih čokolad.

## O datotekah
Na začetku sem imela samo Chocolate\_Collection.docx datoteko, v katero sem sproti zapisovala podatke o zbirki. Nato sem jo s pomočjo .py programov prepisala v .csv. To sem shranila v MySql bazo 'zbiratelj' (https://github.com/campovski/zbiratelj), kamor sem kasneje dodajala nove podatke in na koncu od tam izvozila datoteko, podobno nove\_cokolade\_barva.csv, le da brez zadnjega stolpca Barva. S programom barva\_cokolade.py sem dodala barvo in nato pri končnem izdelku uporabila nove\_cokolade_barva.csv.
