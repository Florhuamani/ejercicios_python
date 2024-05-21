#Ejercicio Dieciocho*
#Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos contraseñas coincidan.
while True:
    contraseña1=input("Ingrese la contraseña:")
    contraseña2=input("Confirme la contraseña:")
    if contraseña1 == contraseña2:
        print("contraseña confirmada")
        break
    else:
        print("Las contraseñas no coinciden. Inténtelo de nuevo")