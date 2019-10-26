med = 0
chi = 0
gra = 0
n = int(input("Introduce el numero de valores de ventas del vendedor: "))
for i in range(0, n, 1):
    v = float(input("Introduce la venta del vendedor: "))
    if v <= 200:
        chi = chi + 1
    elif v = 400:
        med = med + 1
    else:
        gra = gra + 1
else:
    print(f"Eñ numero de vendas menores a $200 son {chi}, menores a $400 son {med} y mayores a $400 son {gra}")
print("Fin del programa")    

