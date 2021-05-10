"""
entrada
lista=>int=>lista
salida
lista sin #s divisibles por 7
"""
lista=[]
for i in range(1,101):
    if(i%7!=0):
        lista.append(i)
print(lista)