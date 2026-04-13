#ETAPAS:
#Un sistema que consulte la edad, y de acuerdo a ella indique si la persona es mayor de edad o no.
#
#Crear un programa de validación de usuario y contraseña (consultar usuario y contraseña), los únicos dos usuarios conectados son:
#User1: pedro   	Contraseña1: 1234
#User2: angel		Contraseña2: a4s1
#
#Solicitar el ingreso de 3 notas por pantalla, luego calcular el promedio de las 3 notas (cada nota tiene la misma ponderación), finalmente indicar con una salida de pantalla “Aprobado” en el caso de que el promedio sea igual o mayor a 4.0.


# 1

edad = int(input("ingresa tu edad:\n"))

if edad >= 18:
    print("eres mayor de edad")
else:
    print("eres menor de edad")

usuario = input("inrgese su usuario:\n")
contraseña = input("ingrese su contraseña:\n")

if usuario == "pedro" and contraseña == "1234":
    print("Bienvenido Pedro")
elif usuario == "angel" and contraseña == "a4s1":
    print("bienvenido angel")
else:
    print("usuario o contraseña incorrectos")

nota1 = float(input("ingrese su primera nota:\n"))
nota2 = float(input("ingrese su segunda nota:\n"))
nota3 = float(input("ingrese su tercera nota:\n"))

promedio = (nota1 + nota2 + nota3) / 3
print(f"tu promedio es: {promedio}")

if promedio > 4.0:
    print("aprobado")
else:
    print("reprobado")






