# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automatica el precio que debe cobrar a sus 
#clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 puede entrar gratis, si tiene entre 4 y 18 debe pagar 5 soles, y si es mayor de 18 deberá pagar 10 soles.

edad = int(input("Ingrese la edad del cliente: "))

if edad < 4:
    print("El cliente puede entrar gratis.")
elif edad >= 4 and edad <= 18:
    print("El cliente debe pagar 5 soles por la entrada.")
else:
    print("El cliente debe pagar 10 soles por la entrada.")


#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces

palabra = input("Ingresa una palabra: ")

for i in range(10):
    print(palabra)

# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
numero = int(input("Ingresa un número entero positivo: "))

impares = ""
for i in range(1, numero+1, 2):
    impares += f"{i},"
impares = impares[:-1]  # Elimina la última coma

print(impares)

#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
        

#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
palabra = input("Ingresa una palabra: ")

for i in range(len(palabra) - 1, -1, -1):
    print(palabra[i])

# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de la imagen adjunta.
numero = int(input("Ingresa un número entero: "))

for i in range(1, numero + 1):
    for j in range(i * 2 - 1, 0, -2):
        print(j, end=" ")
    print()

    
# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
frase = input("Ingresa una frase: ")
letra = input("Ingresa una letra: ")

contador = 0
for caracter in frase:
    if caracter == letra:
        contador += 1

print(f"La letra '{letra}' aparece {contador} veces en la frase.")

# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

palabra = input("Ingresa una palabra: ")

for i in range(len(palabra) - 1, -1, -1):
    print(palabra[i])
    
#  Escriba un programa que pregunte cuántos números se van a introducir, luego pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el anterior.
cantidad_numeros = int(input("¿Cuántos números vas a introducir?: "))
numeros = [int(input(f"Ingrese el número {i + 1}: ")) for i in range(cantidad_numeros)]

for i in range(1, len(numeros)):
    if numeros[i] <= numeros[i - 1]:
        print(f"El número {numeros[i]} no es mayor que el número anterior.")

# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
frase = input("Ingresa una frase: ")
letra = input("Ingresa una letra: ")

contador = 0
for caracter in frase:
    if caracter == letra:
        contador += 1

print(f"La letra '{letra}' aparece {contador} veces en la frase.")

# Escriba un programa que pregunte cuantos números se van a introducir, pida los esos números (que puedan ser decimales) y calcule su suma, mostrar por terminal la suma de los números introducidos.

cantidad_numeros = int(input("¿Cuántos números vas a introducir?: "))
suma = 0

for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    suma += numero

print(f"La suma de los números introducidos es: {suma}")

#  Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido. 
cantidad_numeros:int = int(input("¿Cuántos números vas a introducir?: "))
numeros_negativos = 0

for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    if numero < 0:
        numeros_negativos += 1

print(f"Has introducido {numeros_negativos} números negativos.")


