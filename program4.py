koszyk = [
    {'produkt': 'mleko smak orzechowy', 'ilosc': 1, 'cena': 1.5, 'alergeny': 'laktoza,orzeszki'},
    {'produkt': 'czekolada', 'ilosc': 2, 'cena': 2.5, 'alergeny' : 'orzeszki'},
    {'produkt': 'jogurt', 'ilosc': 4, 'cena': 3.5,"alergeny" : 'laktoza'}
]

# suma = 0
# for poz in koszyk:
#     il = poz['ilosc']
#     c = poz['cena']
#     suma = suma + (c * il)

p = koszyk[i]
alergeny = p['alergeny'].split(',')
# max=len(koszyk[j])
# while j < max :
for value in variable:
    pass
    if 'laktoza' in alergeny and 'orzeszki' in alergeny:
        print('bingo, dzwon do szpitlaa')
    elif 'laktoza' in alergeny:
        print('lala')
    elif 'orzeszki' in alergeny:
        print('wwwwwwwwwwww')
    else:
        print('bezpieczne jedzenie')

    # j+=1

# if 'alergeny' : 'laktoza' and 'alergeny' : 'orzeszki' :
#     print("nie mozesz kupic")
# elif not 'alergeny': 'laktoza' and 'alergeny' : 'orzeszki' :
#     print("mozesz kupic tylko dla siebie")
# else not 'alergeny' : 'laktoza' and not 'alergeny' : 'orzeszki' :
#     print('nie mozesz kupic takich zakupow')
    # print(c)
    # print(suma)
    # print(poz)
# print(suma)
