archivo = open('paises.txt', 'r')
#Cuente e imprima las ciudades que su pais inicie con la letra E

#Buesque e imprima la Capiltal de Colombia
archivo = open('paises.txt', 'r')
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(a)
archivo.close()

