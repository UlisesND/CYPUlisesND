serie = 0
n = int(input("Introduce un numero entero: "))
band = 't'
for i in range(1, n, 1):
    if band == 't':
        serie = serie + 1/i
        band = 'f'
    else:
        serie = serie - 1/i
        band = 't'
else:
     print(f"El resultado es {serie}")
print("Fin del programa")     
