archivo = open('paises.txt', 'r')
#imprima la posicion del pais de Uganda
Uga=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  Uga=Uga+1 
  if(a=="Uganda: Kampala\n"):
    break
  lista=[]   
print(Uga)
archivo.close()

