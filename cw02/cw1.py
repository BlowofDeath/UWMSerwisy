
lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'

imie = 'Tomaasz'
nazwisko = 'Jablonski'

litera_1 = imie[2]
litera_2 = nazwisko[3]

liczba_1 = lorem.count(litera_1)
liczba_2 = lorem.count(litera_2)




print('W tekście jest ' + str(liczba_1) +  ' liter ' + litera_1 + ' oraz ' + str(liczba_2) + ' liter ' + litera_2)
