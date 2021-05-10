dividendo=int(input("Dividendo: "))
divisor=int(input("Divisor: "))
if dividendo>0 and divisor>0:
  cociente=0
  residuo=dividendo
  while (residuo>=divisor):
    residuo-=divisor
    cociente+=1
print(residuo)
print(cociente)
