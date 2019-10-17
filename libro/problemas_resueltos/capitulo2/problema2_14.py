TIPOENf = int (input("Introduce tu tipo de enfermedad padecida: "))
EDAD = int (input("Introduce tu edad: "))
DIAS = int (input("Introduce el numero de dias que estuviste hospitalizado: "))
if TIPOENF == 1:
    COSTOT = DIAS * 25
elif TIPOENF == 2:
    COSTOT = DIAS * 16
elif TIPOENF == 3:
    COSTOT = DIAS * 20
elif TIPOENF == 4:
    COSTOT = DIAS * 32
if (EDAD >= 4) (EDAD <= 22):
    COSTOT = COSTOT * 1.10
print(f"Costo total: { COSTOT } ")
