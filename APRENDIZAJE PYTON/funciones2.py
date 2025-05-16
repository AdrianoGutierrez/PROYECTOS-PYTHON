#retorno de fuciones
#return
#primera forma de la funcion 
def suma(n1, n2):
    totalSuma = n1 + n2
    print(f"la suma es {totalSuma}")

suma(2, 3)

#segunda forma de la funcion con return
def sumar(n1, n2):
    return n1 + n2

total = sumar(2,3)
total1 = sumar(20, 20)
total2 = total + total1
print(f"el total es {total} y total1 es  {total1} por tanto la suma de sumas es {total2}")
