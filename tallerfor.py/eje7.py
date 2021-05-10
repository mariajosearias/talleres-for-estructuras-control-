archivo = open('paises.txt', 'r')
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U

lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="U"):
    print(i)
archivo = open('paises.txt', 'r')
lista2=[]
pais=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista2.append(i[r])
  a="".join(lista2)
  pais.append(a)
  lista2=[]
for i in pais:
  if(i[0]=="U"):
    print(i)
archivo.close()
