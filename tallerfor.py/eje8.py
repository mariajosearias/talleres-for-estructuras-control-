archivo = open('paises.txt', 'r')
#Cuente e imprima cuantos paises que hay en el archivo
P=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  P=P+1 
  if(a=="Paises\n"):
    break
  lista=[]   
print(P)
archivo.close()

