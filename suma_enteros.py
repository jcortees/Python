"""
Ejercicio 6
Escribir un programa que lea un entero positivo, 
, introducido por el usuario y después muestre en pantalla la suma de todos los 
enteros desde 1 hasta n.
La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
suma=n(n+1)/n
"""

def main():
    numero=int(input("Digite un numero entero positivo: \n"))
    suma=numero*(numero+1)
    resultado=suma/2
    print(resultado)
if __name__ == '__main__':
    main()    