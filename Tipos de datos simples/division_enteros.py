"""
Ejercicio 8
Escribir un programa que pida al usuario dos números enteros y muestre por 
pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> 
son los números introducidos por el usuario, y <c> y <r> son el cociente y 
el resto de la división entera respectivamente.
"""

def main():
    numero_n=int(input("Digite un numero entero: \n"))
    numero_m=int(input("Digite otro numero entero: \n"))

    cociente=numero_n//numero_m
    resto=numero_n%numero_m
    print("cociente: ",cociente)
    print("Resto: ",resto)
        
    
if __name__=='__main__':
    main()