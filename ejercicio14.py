# Ejercicio Catorce*
#Tenemos la pantalla del móvil bloqueada. Partiendo de un PIN_SECRETO, intentaremos desbloquear la pantalla. Tenemos hasta 3 intentos. Simula el proceso con Python. En caso de acceder, lanza al usuario login correcto. Sino, llamando ala policía.
pin_secreto="123"
contador=3
while contador > 0:
	ingresante:str=str(input("ingrese contraseña: "))
	if ingresante == pin_secreto:
		print("login correcto")
		break
	else:
		contador-=1
		print("llamando a la policia")
		continue
	