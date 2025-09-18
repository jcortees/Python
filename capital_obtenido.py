"""
Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a invertir,
el interés anual y el número de años, y muestre por pantalla el capital 
obtenido en la inversión.
"""

def main():
    inversion=float(input("Digite la cantidad a invertir: \n"))
    Interes=float(input("Digite el interes anual: \n"))
    anios=int(input("Digite el numero de años de la inversion: \n"))

    obtenido=inversion*(Interes/100+1)**anios
    print("El capital obtenido en la inversion es: " + str(round(obtenido, 2)))


if __name__ == '__main__':
    main()    