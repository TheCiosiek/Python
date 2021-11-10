lista=[1,2,3,4,5]
lista_max=lista
x1=max(lista)
del lista_max[lista.index(x1)]
x2=lista_max[0]
for i in range (len(lista_max)):
    if lista_max[i]>x2:
        x2=lista_max[i]
print(f"Największa liczba: {x1}\nDruga największa liczba: {x2}")
