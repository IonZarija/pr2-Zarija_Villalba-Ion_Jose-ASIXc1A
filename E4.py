"""
Ion Zarija
José Villalba
09/10/23
ASIXc1A M03 UF1 A2
Programa que dice si tiene la edad suficiente para trabajar
"""
edad = int(input("Introduzca su edad: "))
if edad >= 16 and edad<=65:
    print("Tienes edad para trabajar")
if edad < 16 or edad > 65:
    print("No tiene edad para trabajar")