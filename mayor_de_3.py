NUM1 = float (input ("introduce un numero: "))
NUM2 = float (input ("introduce un numero: "))
NUM3 = float (input ("introduce un numero: "))
if NUM1 < NUM2 and NUM2 < NUM3:
    print(f"El {NUM3} es el mayor")
if NUM1 > NUM2 and NUM2 > NUM3:
    print(f"El {NUM1} es el mayor")
if NUM1 < NUM2 and NUM2 > NUM3:
    print(f"El {NUM3} es el mayor")
print("FIn del programa") 

