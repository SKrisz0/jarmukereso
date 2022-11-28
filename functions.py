from data import *
from os import system

filename = 'data.py'
cimsor = ''

def menu():
    system('cls')
    print('Milyen jellegű autót keres?')
    print('a - Kilépés')
    print('b - Sport')
    print('c - Családi, kisbusz')
    print('d - Terepjáró')
    print('e - Tuningok, extrák')
    return input('Kérem írja be a választott típus sorszámát: ')

def loadSport(choises):
    system('cls')
    file = open(filename, 'r', encoding='utf-8')
    fulldata = ''
    
    
    if choises == '1':
        data = szuperSport
    elif choises == '2':
        data = muscle
    elif choises == '3':
        data = sport
    elif choises == '4':
        data = hetszem
    elif choises == '5':
        data = nyolcszem
    elif choises == '6':
        data = kilencszem
    elif choises == '7':
        data = nehezterep
    elif choises == '8':
        data = varossuv
    elif choises == '9':
        data = legszurok
    elif choises == '10':
        data = ledek
    elif choises == '11':
        data = spoiler
    elif choises == '12':
        data = felnik
    elif choises == '13':
        data = turbok
    
        
    for entry in data:
        fulldata += 'Márka: '+entry['marka'].ljust(20)+' Lóerő: '+entry['HP'].ljust(10)+' Ár: '+entry['price']+'\n'
   
    file.close()
    return input(fulldata)

def menuSport():
    system('cls')
    print('Milyen jellgű sportautót keres?')
    print('0 - Vissza a menübe')
    print('1 - Szupersport')
    print('2 - Muscle')
    print('3 - Sport')
    return input('Választásának sorszáma: ')


def menuCsaladi():
    system('cls')
    print('Hány személyes jármű érdekli?')
    print('0 - Vissza a menübe')
    print('4 - hét személyes')
    print('5 - nyolc személyes')
    print('6 - kilenc személyes')
    return input('Kérem válassza ki hány személyes járműre van szüksége: ')

def menuTerepjaro():
    system('cls')
    print('Milyen jellegű terepjáró érdekli?')
    print('0 - Vissza a menübe')
    print('7 - Nehéz terepre való terepjáró')
    print('8 - Városi terepjáró')
    return input('Választásának sorszáma: ')

def menuExtrak():
    system('cls')
    print('Milyen extrákra lenne szüksége?')
    print('0 - Vissza a menübe')
    print('9 - Légszűrők')
    print('10 - LED-ek')
    print('11 - Spoiler tartozékok')
    print('12 - Felnik')
    print('13 - Turbók')
    return input('Kérem írja be a tuning sorszámát, ami érdekli: ')
