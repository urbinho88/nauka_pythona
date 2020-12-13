

koszyk = {'product': ['mleko','czekolada'],
        'ilosc': [1,2],
        'cena': [1.5,3] }


suma = 0

produkty = koszyk['product']
ilosci = koszyk['ilosc']
ceny = koszyk['cena']


for i in ranage(len(produkty)):
    print(produkty[i])
    pritt(ilosci[i])
    c = ceny[i]
    suma = suma + c

# for poz in koszyk:
#     il = poz['ilosc'[]]
#     c = poz['cena'[]]
#     suma = suma + (c * il)
print(suma)


# salon = [
#     {'samochod': 'kia', 'ilosc': 1, 'cena': 222215},
#     {'samochod': 'ford', 'ilosc': 2, 'cena': 2533333},
#     {'samochod': 'fiat', 'ilosc': 4, 'cena': 3511111}
# ]
#
# suma = 0
# for poz in salon:
#     il = poz['ilosc']
#     c = poz['cena']
#     suma = suma + (c * il)
#     # print(c)
#     # print(suma)
#     # print(poz)
# print(suma)
#
# koszyk = [
#     {'produkt': 'mleko', 'ilosc': 1, 'cena': 1.5, 'alergeny': []},
#     {'produkt': 'czekolada', 'ilosc': 2, 'cena': 2.5},
#     {'produkt': 'konserwa', 'ilosc': 4, 'cena': 3.5}
# ]
#
# suma = 0
# for poz in koszyk:
#     il = poz['ilosc']
#     c = poz['cena']
#     suma = suma + (c * il)
#     # print(c)
#     # print(suma)
#     # print(poz)
# print(suma)
