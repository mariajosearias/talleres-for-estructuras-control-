archivo = open('paises.txt', 'r')
#Imprima todas las Capitales

lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]

archivo.close()

