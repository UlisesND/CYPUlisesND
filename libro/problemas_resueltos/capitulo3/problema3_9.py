serie = 0 
n = int(input("Introduce el numero de terminos de la serie: "))
for i in range(1, n, 1):
    serie = serie + i**i
else:
    print(f"EL resultdo de la serie es {serie}")
print("Fin del programa")
