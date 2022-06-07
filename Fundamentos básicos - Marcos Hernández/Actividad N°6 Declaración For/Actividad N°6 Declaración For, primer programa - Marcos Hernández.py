#Nombre: Marcos Hernández
#Objectivo: Aprender a usar la estructura repetitiva "For", para repetir unas determinadas
#líneas de código con un límite y condición establecidos.

#Actividad N°6: Declaración For

#1. Realice un programa utilizando for que le solicite al usuario que ingrese una
#cadena de texto, el mismo debe contar la cantidad de espacios, puntos y comas y
#mostrar el resultado total en pantalla.

a = str(input("Ingrese una cadena de texto: "));
espacios = 0;
comas = 0;
puntos = 0;

for b in a:
    if b == " ":
        espacios += 1;
    if b == ",":
        comas += 1;
    if b == ".":
        puntos += 1;

print("\nLa cadena de texto introducida tiene un total de {} espacio(s), {} coma(s) y {} punto(s).".format(espacios, comas, puntos));