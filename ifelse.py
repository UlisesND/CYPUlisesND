edad = int(input("Dame tu edad: "))
INE = bool ( int( input ("Tienes INE? ( 0 NO / 1 SI): ")))
if edad >= 18 and INE == True:
 print ("Es mayor de edad ")
 print ("Puedes entrar al bar")
else:
    print ("Eres menor de edad")
    print ("No puedes entrar")
print ("Fin del programa ")

