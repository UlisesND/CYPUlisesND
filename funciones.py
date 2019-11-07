def sumar(x , y):
    z = x + y
    return z

def restar(x , y):
    return x - y

def mi_print( texto ):
    print(f"Este es mi print: {texto} ")
    
def multiplica(valor, veces):
    if veces == None :
        print("Deves enviar el segundo argumento de la funcion")
    else:
        print(valor * veces)

def comanda(mesa , comensal , entrada , medio , fuerte , postre="gelatina de limon"):
    print(f"Mesa: {mesa} comensal:{comensal}")
    print(f"\t Entrada: {entrada}")
    print(f"\t segundo tiempo: {medio}")
    print(f"\t plato fuerte: {fuerte}")
    print(f"\t postre: {postre}")
def imprime_argumentos(*argumentos):
   for index in range (len(argumentos)):
       print(argumentos[index ])
def comanda2(**comida):
    llaves = comida.keys()
    for elem in llaves:
        print(elem, "->", comida[elem])
    
a = 10
b = 5
c = sumar(a,b)
print(f"la suma de {a} y {b} es {c}")
c = restar(a,b)
print(f"la suma de {a} y {b} es {c}")
mi_print("hola")
multiplica(10, None)
multiplica (10, 3)
multiplica ('hola' , 3)
comanda(2, 1,"Ensalada", "Sopa de rana", "Filete de Oso", "Flan")
comanda("Ensalada", "Sopa de rana", "Filete de Oso", "Flan", 2, 1)
comanda(entrada="Ensalada", medio="Sopa de rana", fuerte="Filete de Oso", postre="Flan", mesa=2, comensal=1)
comanda(entrada="Ensalada", medio="Sopa de rana", fuerte="Filete de Oso", mesa=2, comensal=1)
imprime_argumentos('hola', True, 3.1416, 1000, {'id': 'sc01','nombre':'juna'})
comanda2(entrada="Ensalada", medio="Sopa de rana", fuerte="Filete de Oso", mesa=2, comensal=1, postre="Srudel de manzana", bebida='coca ligth')
