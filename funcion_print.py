#print tiene 4 formas de uso
"""
1.- con comas
2.- con signo '+'
3.- con la funcion format ()
4.- es una variantr de format ()
"""
# con comas , concatenar agregagando
# un espacio y haciendo casting de tipo 
edad = 10
nombre = "Juan"
estatura = 1.67
print (edad , estatura, nombre)
#con '+' hace lo mismo pero no
#hace elcasting automatico
#no agrega espacio
print (str (edad) + str (estatura) + nombre)
#funcion format ()
print ("nombre: {} edad:{}".format(nombre, edad))
#4.- con una variante de format () simplificada
print (f"Nombre: \"{nombre}\" \nEdad:\t {edad}")

#print y el argumento end
print ("solo hay 10 tipos de personas las que saben binario y las que no", end= " ")
print ("como que 10?") 
