"""
Ion Zarija
José Villalba
Omar Vargas
09/10/23
ASIXc1A M03 UF1 A2
Escriu un programa que al introducir 5 números, muestra si el 5o está en el rango del 1o,2o y 3o,4o
"""
list = []
for x in range (5):
    num = int(input("Introduce un valor: "))
    list.append(num)
if (list[4] >= list[0] and list[4] <= list[1]) or (list[4] <= list[0] and list[4] >= list[1]):
    print("TRUE (El número está incluído en el primer rango)")
else:
    print("FALSE (El número no está incluído en el primer rango)")
if (list[4] >= list[2] and list[4] <= list[3]) or (list[4] <= list[2] and list[4] >= list[3]):
    print("TRUE (El número está incluído en el segundo rango)")
else:
    print("FALSE (El número no está incluído en el segundo rango)")