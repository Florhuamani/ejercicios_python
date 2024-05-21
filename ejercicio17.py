# *Ejercicio Diecisiete*
# Crea un programa en Python que simule el funcionamiento de un cajero automático. El programa debe permitir al usuario realizar las siguientes operaciones:
 
# - Verificar el saldo de su cuenta.
# - Depositar dinero en su cuenta.
# - Retirar dinero de su cuenta.
# - Salir del programa.
# El programa debe iniciar con un saldo inicial predeterminado y mostrar un menú con las siguientes opciones:
 
# - Verificar saldo
# - Depositar dinero
# - Retirar dinero
# - Salir
saldo = 1000

while True:
    print("\nMenú de opciones:")
    print("1. Verificar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        print(f"Su saldo actual es: ${saldo}")
    elif opcion == '2':
        cantidad_deposito = float(input("Ingrese la cantidad a depositar: $"))
        saldo += cantidad_deposito
        print(f"Se han depositado ${cantidad_deposito}. Su saldo actual es ${saldo}")
    elif opcion == '3':
        cantidad_retiro = float(input("Ingrese la cantidad a retirar: $"))
        if cantidad_retiro <= saldo:
            saldo -= cantidad_retiro
            print(f"Se han retirado ${cantidad_retiro}. Su saldo actual es: ${saldo}")
        else:
            print("Saldo insuficiente para realizar el retiro.")
    elif opcion == '4':
        print("¡Gracias por utilizar el simulador de cajero automático!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

