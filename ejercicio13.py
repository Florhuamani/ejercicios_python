# Vamos a diseñar una calculadora que se enciende y hasta que no tecleamos SAL no se apaga.
 
# Esta calculadora funciona de la siguiente manera:
# - Recogemos los datos A y B
#- Si operación es 1 calcula la raíz cuadrada de la suma de A y B
# - Si operación es 2 calcula A / B. Vigilamos que B no sea 0...
# - Si la operación es 3 calculamos la siguiente fórmula: ( A * B ) / 2.5
#Calculadora que se enciende hasta que se teclee 'SAL'
while True:
    print("Calculadora encendida.")
    operacion = input("Ingrese el número de operación (1, 2 o 3) o 'SAL' para apagar: ")
    
    if operacion == "SAL":
        print("Calculadora apagada.")
        break
    
    if operacion in ["1", "2", "3"]:
        A = float(input("Ingrese el valor de A: "))
        B = float(input("Ingrese el valor de B: "))
        
        if operacion == "1":
            resultado = (A + B) == 0.5
        elif operacion == "2":
            if B != 0:
                resultado = A / B
            else:
                print("Error: No se puede dividir por cero.")
                continue
        elif operacion == "3":
            resultado = (A * B) / 2.5
        
        print("El resultado es:", resultado)
    else:
        print("Operación no válida. Por favor, ingrese 1, 2, 3 o 'SAL'.")

