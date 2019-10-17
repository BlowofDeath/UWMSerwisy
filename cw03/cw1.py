lista1 = [1,2,3,4,5,6,7,8,9];
lista2 = [1,2,3,4,5,6,7,8,9];

def func(l1, l2):
    tab = {'parzyste':[],'nieparzyste':[]};
    for i in lista1:
        if i % 2 == 0:
            tab['parzyste'].append(i);
    for j in lista2:
        if i % 2 != 0:
            tab['nieparzyste'].append(j);
    return  tab;


wynik = func(lista1, lista2);
print(wynik);

