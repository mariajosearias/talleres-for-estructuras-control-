archivo = open('paises.txt', 'r')
#Busque e imprima el pais de Venezuela y su capital

lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  if(a=="Venezuela: Caracas\n"):
    break
  lista=[]   
print(a)
archivo.close()

