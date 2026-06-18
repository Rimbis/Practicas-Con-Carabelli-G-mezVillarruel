"""
#Suma, resta, division, multiplicacion

num1=4
num2=5

suma = (num1 + num2)
print (suma)

resta = (num1 - num2)
print (resta)

multiplica = (num1 * num2)
print (multiplica)

divide = (num1 / num2)
print ( "Estoo es division ", divide)


#Mensaje personalizado

nombre = input(str("Mi nombre es:..."))
print (f"Hola buenos días, tardes y noches {nombre}")

#Sumas float e int

numero = int(input())
numerito = float(input())
sumaNumeritos = numero + numerito

print (f"Tu total es: {sumaNumeritos}")

#Base*altura

base = int(input("Agregue base:"))
altura = int(input("Agregue altura:"))
area = base * altura
print (f"Base x altura= Area: {area}")

#Promedio

Nota1 = float(input("Agregue la primera: "))
Nota2 = float(input("Agregue el segundo: "))
Nota3 = float(input("Agregue el tercero: "))
Promedio = (Nota1 + Nota2 + Nota3) / 3
print (f"Tu promedio es: {Promedio}")

#Concatenar texto

nombre = "José Luis"
apellido = "Lopez"
espacio = " "
completo = nombre + espacio + apellido

print (f"Holi {nombre} {apellido}")
print ("Holi", nombre, apellido)
print ("Holi", completo)
print ("hola", nombre, espacio, apellido)

#String

Ejemplo = input(str("ingrese para modificar:"))
print (Ejemplo.upper())
print (Ejemplo.lower())
print (Ejemplo.title())

#LEN CONTAR LETRAS

ej = input(str("Ingrese un texto:"))
print(f"la palabra tiene", len(ej), "caracteres")

#Mayor de edad

edad = int(input("ingrese su edad porfa:"))

if (edad >=18):
    print("eres mayor de edad")
else:
    print("eres menor de edad")

#if elif else
    
numero = int(input("ingrese su numero:"))

if (numero >0):
    print("es positivo")
elif (numero == 0):
    print("es cero")
else:
    print("es negatvo")

#modulos par/impar
    
numerin = int(input("ingrese un numero:"))


if (numerin % 2 == 0):
    print ("Es par")
else:
    print ("Es impar")

"""
#Calculadora simple con if
    
num1= int(input("Ingrese el primer numero"))
num2= int(input("Ingrese el segundo numero"))
elegir = input(str("Ingresar opcion"))

if (elegir == "+"):
    print (num1 + num2)
elif (elegir == "-"):
    print (num1 - num2)
elif (elegir == "*"):
    print (num1 * num2)
else:
    print (num1 / num2)

#Nota final excelente 
    
nota = int(input("Ingrese su nota final: "))

if(nota >=9):
    print ("Excelente")
elif(nota >=7):
    print ("Aprobado")
elif(nota >=5):
    print ("Regular")
else:
    print ("Desaprobado")
