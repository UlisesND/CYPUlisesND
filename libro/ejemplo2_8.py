CATE = int (input ("Escoge la categoria de empleado "))
SUE = float (input ("Dime cual es tu sueldo "))
if CATE == 1:
    NSUE = SUE * 1.15
    print (f"Su nuevo sueldo es de ${NSUE} y la categoria es {CATE}")
elif CATE == 2:
    NSUE = SUE * 1.10
    print (f"Su nuevo sueldo es de ${NSUE} y la categoria es {CATE}")
elif CATE == 3:
    NSUE = SUE * 1.08
    print (f"Su nuevo sueldo es de ${NSUE} y la categoria es {CATE}")
elif CATE == 4:
    NSUE = SUE * 1.07
    print (f"Su nuevo sueldo es de ${NSUE} y la categoria es {CATE}")
else:
    print ("Su valor no es valido")
print ("Fin del programa")

