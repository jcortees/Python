"""
Ejercicio 7
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
calcule el índice de masa corporal y lo almacene en una variable, y muestre por
pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice 
de masa corporal calculado redondeado con dos decimales.
"""

def main():
    peso=float(input("Ingrese su peso en Kg: \n"))
    estatura=float(input("Ingrese su estatura en metros: \n"))
    imc=peso/(estatura)**2
    print("Tu indice de masa coporal es : " ,f"{imc:.2f}")

if __name__=='__main__':
    main()    