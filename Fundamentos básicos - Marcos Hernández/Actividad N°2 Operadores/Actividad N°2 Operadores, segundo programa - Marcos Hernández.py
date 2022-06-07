#Nombre: Marcos Hernández
#Objectivo: Aprender a usar correctamente los operadores en Python. Ya sea para establecer 
#u evaluar condiciones.


#Actividad N°2: Operadores

#2. Ejecute la siguiente expresión de comparación: ¿Qué valor devuelve la expresión?
#   11 > 4 < 5 and 3 < 2 or 2 != 4 and 4 == 2 + 2 or not True
#
#Para demostrar la compresión de los operadores utilizados debe incluir
#el desarrollo manual del caso propuesto (puede incluir una foto) donde demuestre
#como obtuvo el resultado.


#Variables   pxp = Parte por parte

print("\n//////Expresión a resolver: 11 > 4 < 5 and 3 < 2 or 2 != 4 and 4 == 2 + 2 or not True//////\n\n");

pxp = 11 > 4 < 5 and 3 < 2;
print("Primera parte a desglosar: 11 > 4 < 5 and 3 < 2\nResultado ----> ", pxp, "\n\nPresiona la tecla ENTER para continuar...\n");
input();

pxp = 2 != 4 and 4 == 2 + 2;
print("Segunda parte a desglosar: 2 != 4 and 4 == 2 + 2\nResultado ----> ", pxp, "\n\nPresiona la tecla ENTER para continuar...\n");
input();

pxp = not True;
print("Tercera parte a desglosar: not True\nResultado ----> ", pxp, "\n\nPresiona la tecla ENTER para continuar...\n");
print("\n\n///Más pruebas///\n\n");
input();

pxp = 11 > 4 < 5 and 3 < 2 or 2 != 4 and 4 == 2 + 2;
print("Parte combinada uno: 11 > 4 < 5 and 3 < 2 or 2 != 4 and 4 == 2 + 2\nResultado ----> ", pxp, "\n\nPresiona la tecla ENTER para continuar...\n");
input();

pxp = 2 != 4 and 4 == 2 + 2 or not True;
print("Parte combinada segundo: 2 != 4 and 4 == 2 + 2 or not True\nResultado ----> ", pxp, "\n\nPresiona la tecla ENTER para continuar...\n");
input();

print("\n\n///En conclusión///\n\n");

pxp = 11 > 4 < 5 and 3 < 2 or 2 != 4 and 4 == 2 + 2 or not True;
print("Esta expresión dará siempre True: 11 > 4 < 5 and 3 < 2 or 2 != 4 and 4 == 2 + 2 or not True\nResultado ----> ", pxp, "\n\nPresiona la tecla ENTER para continuar...\n");
input();

pxp = 2 != 4 and 4 == 2 + 2 or 11 > 4 < 5 and 3 < 2 or not True;
print("Como bonus, observen lo que pasa si cambiamos de ubicación una parte: 2 != 4 and 4 == 2 + 2 or 11 > 4 < 5 and 3 < 2 or not True\nResultado ----> ", pxp, "\n\nPresiona la tecla ENTER para continuar...\n");
input();

print("\n\n///FIN///\n\n");