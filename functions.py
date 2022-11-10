from data import *
from os import system

filename = 'data.csv'
cimsor = ''

def menu():
    system('cls')
    print('Milyen jellegű autót keres?')
    print('0 - Mindegy')
    print('1 - Sport')
    print('2 - Couple')
    print('3 - Családi')
    print('4 - Terepjáró')
    print('5 - Városi SUV')
    return input('Kérem írja be a választott típus sorszámát: ')

def loadCars():
    file = open(filename, 'r', encoding='utf-8')
    global cimsor
    cimsor = file.readline()
    for row in file:
        splitted = row.strip().split(';')
        cars[splitted[0]] = int(splitted[1])
    file.close()