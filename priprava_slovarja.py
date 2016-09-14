import re
import os

def pripravi_slovar(): # UTF8 !!
    k = 0
    vhod = open("project.csv", 'r')
    slovar_proizvajalcev = {}
    a = re.compile('(.*?)\|.*')
    for vrstica in vhod:
        proizvajalec = a.match(vrstica).group(1)
        if k == 0: k = k + 1
        else:
            if proizvajalec in slovar_proizvajalcev:
                pass
            else:
                slovar_proizvajalcev[proizvajalec] = k
                k = k + 1
    return(slovar_proizvajalcev)

slovar_proizvajalcev = pripravi_slovar()

def zapisi_slovar():
    try: os.remove("proizvajalci.csv")
    except: pass
    izhod = open("proizvajalci.csv", 'w')
    k = 1
    for k  in range(len(slovar_proizvajalcev)+1):
        for kljuc, vrednost in slovar_proizvajalcev.items():
            if k == vrednost:
                izhod.write(str(vrednost)+","+kljuc+"\n")
            else: pass
    
    
