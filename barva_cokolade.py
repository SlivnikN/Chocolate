import re
import os

def dodaj_barvo():
	try: os.remove("nove_cokolade_barva.csv")
	except: pass
	vhod = open("nove_cokolade_test.csv", 'r')
	izhod = open("nove_cokolade_barva.csv", 'w')
	n = 0
	for vrsta in vhod:
		if n == 0:
			izhod.write(vrsta.strip() + "|" + "Barva" + "\n")
			n = n + 1
		else:
			# temna
			if "Noir" in vrsta or "Dark" in vrsta or "Eddel" in vrsta or "Nero" in vrsta or "Temna" in vrsta or "Feinherb" in vrsta:
				izhod.write(vrsta.strip() + "|" + "Dark" + "\n")
			# mlecna
			elif "Lait" in vrsta or "Milk" in vrsta or "Mlečna" in vrsta or "Vollmilch" in vrsta or "Leite" in vrsta or "Latte" in vrsta:
				izhod.write(vrsta.strip() + "|" + "Milk" + "\n")
			# bela
			elif "Blanc" in vrsta or "White" in vrsta or "Weisse" in vrsta or "Bela" in vrsta or "Bianco" in vrsta:
				izhod.write(vrsta.strip() + "|" + "White" + "\n")
			else:
				izhod.write(vrsta.strip() + "|" + "Unknown" + "\n")
	izhod.close()
			
dodaj_barvo()
