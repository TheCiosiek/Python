lista1=[1,2,3,4,5]
lista2=[1,2,3,4,5]
lista3=[1,2,2,3,3,4,5]

set1=set(lista1)
set2=set(lista2)
set3=set(lista3)

if (set1 | set2) ^ set3 or set1 ^ (set2 | set3):
    print("Listy nie zawierają tych samych elementów, ",end='')
else:
    print("Listy zawierają te same elementy, ",end='')
if len(set1)-len(lista1):
    print("lista1, ",end='')
if len(set2)-len(lista2):
    print("lista2, ",end='')
if len(set3)-len(lista3):
    print("lista3 ",end='')

print("zawiera duplikaty.")  