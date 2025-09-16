"""
Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas 
y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
"""
horas_trabajadas=int(input("Digite el numero de horas trabjadas: \n"))

coste_hora=float(input("Digite el coste de las horas: \n"))

pago=horas_trabajadas*coste_hora

print(pago)
