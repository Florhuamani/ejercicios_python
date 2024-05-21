# Ejercicio Quince*
#Crea un algoritmo para la sucesión de Fibonacci. La sucesión de Fibonacci es la siguiente serie:
 
#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
 
# Pista: Empezando por 0 y 1, el siguiente número es la suma de los dos números últimos
# Algoritmo para la sucesión de FIBONACCI
num_uno,num_dos=0,1
while num_dos < 90 :
    print(num_uno,num_dos,end="")
    num_uno+=num_dos
    num_dos+=num_uno