"""
Ion Zarija
José Villalba
Omar Vargas
09/10/23
ASIXc1A M03 UF1 A2
Programa que pide el diámetro de una pizza y devuelve la superficie
"""
import math
dPizza = int(input("Introduzca el diámetro de su pizza: "))
sPizza = math.pi * (dPizza/2)**2
print(f"La superfície de su pizza es {sPizza:.2f} cm²")
