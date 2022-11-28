from functions import *
from data import *

choise = ''
call = ''
while choise != 'a':
    choise = menu()
    if choise == 'b':
        call = menuSport()
    elif choise == 'c':
        call = menuCsaladi()
    elif choise == 'd':
        call = menuTerepjaro()
    elif choise == 'e':
        call = menuExtrak()
            
    if call:
        loadSport(call)
