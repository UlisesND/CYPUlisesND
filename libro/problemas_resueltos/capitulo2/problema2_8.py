COMPRA = float (input("Ingresa tu monto de compra: "))
if COMPRA < 500 :
    PAGAR = COMPRA
else:
    if COMPRA <= 1000 :
        PAGAR = COMPRA - (COMPRA +0.05)
    else:
        if COMPRA <= 7000 :
            PAGAR = COMPRA - (COMPRA * 0.11)
        else:
            if COMPRA <= 15000 :
                PAGAR = COMPRA - (COMPRA * 0.18)
            else:
                PAGAR = COMPRA - (COMPRA * 0.25)
print(f"El total a pagar es: { PAGAR }")
print(f"Fin del programa")
