Pruebas = float (input("Ingresa el precio del producto basico: "))
if Pruebas > 500 :
    IMP = 20 * 0.30 + (Pruebas - 40) * 0.50
else:
    if Pruebas > 20 :
        IMP = (Pruebas - 20) * 0.30
    else:
        IMP = 0
PRETOT = Pruebas + IMP
print(f"El precio de tu producto es: { Pruebas } y el precio con el impuesto es: { PRETOT }")

