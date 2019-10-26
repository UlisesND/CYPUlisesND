may = -100000
men = 100000
n = int(input("Ingresa un numero entero: "))
for i in range(0, n, 1):
    num = int(input("ingresa un numero entero: "))
    if num > may:
        may = num
    else:
        if num < men:
            men = num
else:
    print(f"El maximo valor es {may} y el minimo valo es {men}")
print("Fin del programa")    
