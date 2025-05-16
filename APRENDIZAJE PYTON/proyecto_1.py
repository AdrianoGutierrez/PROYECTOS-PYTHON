#construir una calcauladora de exponentes, esta calculadora deberá pedir los datos al usuario y mostrar el resultado por consola

print("---------CALCULADORA DE POTENCIAS---------\n")

print("Ingrese la base\n")
base = int(input())

print("ingrese el exponente")
exp = int(input())

#operacion calcular la potencia

pot = base ** exp
print(f"Si la base es: {base} y el exponente es {exp} la potencia es:\n{pot}")



