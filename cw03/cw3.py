def delete(text, letter):
    lista = [char for char in text]
    wynik = ''

    for el in lista:
        if letter != el:
            wynik += el
    return wynik;



napis = 'Testowanie'
print(delete(napis, 'o'))
