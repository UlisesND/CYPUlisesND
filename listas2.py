# arreglos
#lectura
#escritura/ asignacion
#actualizacion: insercion, eliminacion, modificacion
#busqueda

#escritura
frutas = ["Zapote", "Manzana" , "Pera", "Aguaquate", "Durazno", "uva", "sandia"]

#lectura, el selector [indice]
print (frutas[2])
# Lectura con for
#for opcion 1
for indice in range (0,7,1):
    print (frutas[indice])
print ("-------")

# for opcion 2 -- por un iterador each

for fr in frutas:
    print (fr)
#asignacion
frutas[2]="melon"
print (frutas)
#insercion al final
frutas.append("Naranja")
print(frutas)
print(len(frutas))
frutas.insert(2,"limon")
print(frutas)
print(len(frutas))
frutas.insert(0, "mamey")
print(frutas)

#eliminacion con pop
print(frutas.pop())
print(frutas)
print(frutas.pop(1))
print(frutas)


frutas[2]="limon"
frutas.append("limon")
print(frutas)
frutas.remove("limon")
print(frutas)


#ordenamiento
frutas.sort()
print(frutas)
frutas.reverse()
print(frutas)

#busqueda
print(f"El limon esta en la posicion, {frutas.index('limon') }")
print(f"El limon esta {frutas.count('limon')} veces en la lista")

#concatenar
print(frutas)
otras_frutas = ["rambutan","mispero", "liche","pitahaya"]
frutas.extend(otras_frutas)
print(frutas)
# copiar
copia=frutas
copia.append("naranja")
print(frutas)
print(copia)
otracopia = frutas.copy()
otracopia.append("fresa")
otracopia.append("fresa")
print(frutas)
print(otracopia)
