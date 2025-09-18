"""
Ejercicio 11
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de
interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales 
de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa 
que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, 
introducida por el usuario. Después el programa debe calcular y mostrar por 
pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear 
cada cantidad a dos decimales.
"""

def main():
    dinero=int(input("Digite la cantidad de dinero depositada: "))
    interes=0.04
    anio1=dinero*(interes+1)
    anio2=anio1*(interes+1)
    aniio3=anio2*(interes+1)

    print("La cantidad de ahorros al primer año es: "+str(round(anio1,2)))
    print("La cantidad de ahorros al segundo año es: "+str(round(anio2,2)))
    print("La cantidad de ahorros al segundo año es: "+str(round(aniio3,2)))

if __name__ == '__main__':
    main()    