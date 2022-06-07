#Nombres: Marcos Hernández.
#Objectivo: Usar ciclos repetitivos, para una conseguir un resultado en una determinada tarea.

#Actividad N°4: Ciclo While

#1. Le gusta ir al cine todos los fines de semana. Cada vez que va al cine
#se compra una gaseosa, unas palomitas de máiz y su entrada.
#   Si tiene un presupuesto de $60 al mes para ir al cine, ¿cuántas veces puede
#ir al cine? Solucione el problema utilizando While.

#Asumiendo que los precios son los siguientes:
#Cine: $5
#Palomitas: $3.75
#Gaseosa: $2.25



#Uso la función de "sleep" (dormir en inglés) de la librería "time" para que el usuario vea
#como se va "actualizando" la suma total, para así calcular cuantas veces se puede ir al cine.

from time import sleep

preciostotal = 11.0;
vecesquepuedoir = 0;

print("Se calculará la cantidad de veces que se puede ir al cine, con un presupuesto de $60\n");

while (preciostotal <= 60):
    print("Suma total: $", preciostotal);
    sleep(1);
    preciostotal += 11.0;
    vecesquepuedoir +=1;

print("\nLa cantidad de veces que puedo ir al cine son:", vecesquepuedoir);