A = int (input("Introduce un numero entero"))
B = int (input("Introduce un numero entero"))
C = int (input("Introduce un numero entero"))
if A < B:
    if B < C:
        print("Los numeros estan de forma creciente")
    else:
        print("Los numeros no estan de forma creciente")
else:
    print("Los numeros no estan de forma creciente")
print("Fin del programa")
