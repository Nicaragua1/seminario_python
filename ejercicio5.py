bienvenida = ("Bienvenido!  \n"
"1: ingresar numeros \n"
"2: ordenar numeros\n"
"3: calcular maximo \n"
"4: calcular minimo \n"
"5: calcular promedio \n"
"0: salir \n")
print(bienvenida)

lista_numeros = [2,2,2,2,2,1]
opcionElegida = int(input("Ingrese opcion: "))
while(opcionElegida != 0):
    if opcionElegida == 1:
        lista_numeros.append(int(input("ingrese un num: ")))
        print(lista_numeros)
    elif opcionElegida == 2:
        lista_numeros.sort
        print("ordenados")
    elif opcionElegida == 3:
        print(max(lista_numeros))
    elif opcionElegida == 4:
        print(min(lista_numeros))
    elif opcionElegida == 5:
        print(sum(lista_numeros) / (len(lista_numeros)))

    opcionElegida = int(input("Ingrese otra opcion: "))
