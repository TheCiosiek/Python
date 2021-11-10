lista=[1,2,3,4,5]
odwrocona_lista=[]
for i in range(len(lista),0,-1):
      odwrocona_lista.append(lista[i-1])
print(f"{odwrocona_lista}")   
