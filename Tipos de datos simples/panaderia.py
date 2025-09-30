"""
Ejercicio 12
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día 
tiene un descuento del 60%. Escribir un programa que comience leyendo el número 
de barras vendidas que no son del día. Después el programa debe mostrar el precio 
habitual de una barra de pan, el descuento que se le hace por no ser fresca y el 
coste final total.

"""

def main():
    pan=3.49
    pan_no_fresco=int(input("Digite el numero de barra vendidas de pan que no son del dia: "))
    descuento=0.6
    total=pan_no_fresco*pan*descuento
    print("El descuento es: ", descuento*100)
    print("El precio del pan es: ",pan)
    print("El precio total es: ",total)

if __name__ == '__main__':
    main()