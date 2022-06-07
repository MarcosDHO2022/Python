#Nombre: Marcos Hernández
#Objectivo: Aprender a usar las listas, así mismo como añadir más objectos a la lista o quitarlos.

#Actividad N°5: Listas

#Crear una lista de compra que le permita:
# * Añadir tantos productos como usted elija.
# * Debe poder verificar si un producto ya está dentro de su lista.
# * Debe mostrar la lista final completa.



print("Bienvenido a nuestro programa para crear listas de compra. Por favor, anote que productos usted desea\ncomprar en su lista.")

control = 0
productos = []
nitem = 1  #Empieza con el número uno, ya que, al iniciar el programa, se comienza con el primer producto para la lista.

while control == 0:
    item = str(input("\nNombre del producto número {}: ". format(nitem)))
    item = item.lower();
    if item in productos and nitem > 1:
        #Aquí intenté con .pop, pero solo funciona con números y no Strings. Además de que se eliminará el elemento que se introdujo antes.
        print("Ya tiene este item en la lista");
    else:
        productos.append(item);
        p = str(input("¿Desea agregar otro producto a la lista? Si o No \n"));
        p = p.lower();
        if p == "no":
            break
        nitem += 1;

print("\nListo, aquí está su lista de compra, que tiene un total de {} productos: ". format(nitem), *productos)