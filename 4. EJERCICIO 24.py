#Capitulo 4. Ejercicio propuesto 24

A = float(input("Ingrese el peso de la esfera A: "))
B = float(input("Ingrese el peso de la esfera B: "))
C = float(input("Ingrese el peso de la esfera C: "))

# Comparamos los pesos para encontrar la esfera más pesada
if A > B and A > C:
    print("La esfera de mayor peso es: A")
elif B > A and B > C:
    print("La esfera de mayor peso es: B")
elif C > A and C > B:
    print("La esfera de mayor peso es: C")
else:
    print("No hay una única esfera más pesada")
