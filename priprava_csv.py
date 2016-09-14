import re
import os

def naredi_csv():
    try: os.remove("test.csv")
    except: pass
    txt = open("test_vmesni.txt", 'r')
    csv = open("test.csv", 'w')
    proizvajalec = ""
    zbirka = ""
    podzbirka = ""
    ime = ""
    for vrstica in txt:
        if vrstica[0] == "#":
            proizvajalec = vrstica[1:].strip()
            zbirka = ""
            podzbirka = ""
        elif vrstica[0] == "*":
            zbirka = vrstica[1:].strip()
            podzbirka = ""
        elif vrstica[0] == "$":
            podzbirka = vrstica[1:].strip()
        elif vrstica == "\n":
            pass
        else:
            ime = vrstica.strip()
            string = proizvajalec + "|" + zbirka + "|" + podzbirka + "|" + ime + "\n"
            csv.write(string)
    csv.close()

def popravi_word():
    try: os.remove("test_vmesni.txt")
    except: pass
    vhod = open("Chocolate_Collection.txt", 'r')
    izhod = open("test_vmesni.txt", 'w')
    k = 0
    for vrstica in vhod:
        if k == 0:
            izhod.write(vrstica[1:])
            #izhod.write(vrstica[3:])
            k = 1
        else: izhod.write(vrstica)
    izhod.close
    
def popravi_csv():
    try: os.remove("project.csv")
    except: pass
    a = []
    vhod = open("test.csv", 'r')
    vhod_text = vhod.read()
    izhod = open("project.csv", 'w')
    regex = re.compile('(.*?),\s(\d+)')
    izhod.write("Proizvajalec|Zbirka|Podzbirka|Ime|Zaporedna številka\n") 
    for match in regex.finditer(vhod_text):
        izhod.write(match.group(1)+"|"+match.group(2)+"\n")
    try: os.remove("test_vmesni.txt")
    except: pass
    try: os.remove("test.csv")
    except: pass

popravi_word()
naredi_csv()
popravi_csv()
