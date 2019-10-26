num = int(input("Introduce un numero entero: "))
if num > 0:
    while(num != 1):
        print(num)
        if (-1)** num > 0:
            num = num / 2
        else:
            num = (num*3) +1
     else: 
         print (num)
else:
    print("EL nimero tiene que ser un entro positivo")
print("Fin del programa")    
