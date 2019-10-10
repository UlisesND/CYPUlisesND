A = int(input("introduce un numero entero"))
B = int(input("introduce un otro numero entero positivo"))
C = int(input("introduce un otro numero entero positivo"))
if A > B:
    if A > C:
        print (f"{A} es el mayor")
    elif A == C:
        print(f"{A} y {C} son iguales, y son los mayores")
    else:
        print(f"{C} es el mayor")
elif A == B:
    if A > C:
        print(f"{A} y {B} son iguales, y los mayores")
    elif A == C:
        print("los tres son iguales a {B}")
    else:
        print(f"{C} es el mayor")
elif B > C :
    print(f"{B} es el mayor")
elif B == C:
    print(f"{B} y {C} son iguales, y los mayores")
else:
    print(f"{C} es el mayor")
print("fin del programa")
       
