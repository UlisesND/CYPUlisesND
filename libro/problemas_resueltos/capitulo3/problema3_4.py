nom = 0 
sue = float(input("Introduce el sueldo del trabajador:"))
while(sue != (-1)):
    if sue < 1000:
        nsue = sue*1.15
    else:
        nsue = sue*1.12
    nom = nom + nsue
    print(f"El nuevo sueldo del trabajador es ${nsue}")
    sue = float(input("introduce el sueldo del trabajador: "))
else:
    print(f"EL nuevo sueldo de los trabajadores es ${nom}")
print("Fin del programa")
