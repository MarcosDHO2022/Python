#Nombres: Marcos Hernández
#Objectivo: Comprender el uso de las condicionales, como el "if", "elif" y "else".

#Actividad N°3: Condicionales

#3. Cree un programa que le permita a un usuario saber que celular
#puede comprar, debe considerar las siguentes opciones.

d = input("¿Desea tener un Android o iOS?\n")

if (d == "Android"):
    d = input("\n¿Tienes dinero?\n")
    if (d == "Si"):
        d = input("\n¿Le importa la cámara?\n")
        if (d == "Si"):
            print("\nGoogle Pixel")

        else:
            print("\nAndroid 11 Go")

    else:
        input("\nDebe comprar un Android de segunda $100.00")

elif (d == "iOS"):
    d = input("\n¿Tienes dinero?\n")
    if (d == "Si"):
        print("IPhone 11");

    else:
        print("\nDebe comprar un IPhone de segunda mano.");