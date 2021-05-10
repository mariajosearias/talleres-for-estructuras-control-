archivo = open('paises.txt', 'r')
#imprima la posicion del pais de Mexico
M=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  M=M+1 
  if(a=="México: Ciudad de México \n"):
    break
  lista=[]   
print(M)
archivo.close()
