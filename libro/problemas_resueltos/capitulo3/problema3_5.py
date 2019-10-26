sumotr = 0
sumpos = 0
cuepos = 0
n = int(input("Introduce un numero entero: "))
for i in range (0, n, 1):
    num = int(input("Introduce un numero entero: "))
    if num > 0:
        sumpos = sumpos + num
        cuepos = cuepos + 1
    else:
        sumotr = sumotr + num
else:
    progen = (sumpos+sumotr)/n
    propos = (sumpos/cuepos)
    print(f"Los numeros positivos son {cuepos}, el promedio de los numeros positivos es {propos} y el promedio general de los numeros es {progen}")
print("Fin del programa")    
