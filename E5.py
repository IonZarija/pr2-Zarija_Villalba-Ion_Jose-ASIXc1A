"""
Ion Zarija
José Villalba
09/10/23
ASIXc1A M03 UF1 A2
Programa que al intoducir una palabra, canvie las vocales por números ( a=1 )
"""
pal = str(input("Introduzca una palabra: "))
pal = pal.replace("a", "1")
pal = pal.replace("e", "2")
pal = pal.replace("i", "3")
pal = pal.replace("o", "4")
pal = pal.replace("u", "5")
pal = pal.replace("A", "1")
pal = pal.replace("E", "2")
pal = pal.replace("I", "3")
pal = pal.replace("O", "4")
pal = pal.replace("U", "5")
print("Su palabara queda como: ", pal)