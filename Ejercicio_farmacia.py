# IMPORTAMOS LA LIBRERIA DEL SISTEMA PARA LIMPIAR LA PANTALLA
import os 
os.system("cls")

# PRIMERO DEFINIMOS LAS VARIABLE QUE UTILIZAREMOS
cant_vendidos = [0,0,0,0]

def es_numerico(string):
    try:
        int(string)
        return True
    except:
        return False

def Append_python(lista,valor,Z):
    A=0
    while A<len(lista):
        if A==Z:
            lista[Z]=lista[Z]+valor
        A=A+1
    return lista

def cantidad_de_ventas(lista):
    print("--------------------------------------")
    print("---------NÚMERO DE VENTAS-------------")
    print("1) Cetirizina:",lista[0], "unidades   ")
    print("2) Fexofenadina:",lista[1], "unidades ")
    print("3) Loratadina:",lista[2], "unidades   ")
    print("4) Desloratadina:",lista[3], "unidades")
    print("--------------------------------------")
    return 0

def total_de_ventas(lista):
    print("-----------------------------------")
    print("---------TOTAL DE VENTAS-----------")
    print("1) Cetirizina:",lista[0]*14990, "CLP")
    print("2) Fexofenadina:",lista[1]*13499, "CLP")
    print("3) Loratadina:",lista[2]*5500, "CLP")
    print("4) Desloratadina:",lista[3]*8390, "CLP")
    print("----------------------------------")
    return 0

def mas_vendido(lista):
    Z=0
    cont=0
    while Z<len(lista):
        if lista[Z]>cont:
            cont=lista[Z]
        Z=Z+1
    Z=0
    while Z<len(lista):
        if lista[Z]==cont:
            cantidad=Z
            Z=len(lista)+1
        Z=Z+1
    if cantidad==0:
        nombre="Cetirizina"
    elif cantidad==1 :
        nombre="Fexofenadina"
    elif cantidad==2:
        nombre="Loratadina"
    else:
        nombre="Desloratadina"
    print("-------------------------------------------------------------------")
    print("El medicamento más vendido es:",nombre, "con ",cont,"unidades")
    print("-------------------------------------------------------------------")
    return 0

def total_vendido(lista):
    Z=0
    cont=0
    while Z<len(lista):
        cont=cont+lista[Z]
        Z=Z+1
    print("--------------------------------------")
    print("El total general de ventas es:",cont)
    print("--------------------------------------")
    return 0

def menos_vendido(lista):
    Z=0
    contador=9999999
    while Z<len(lista):
        if lista[Z]<contador:
            contador=lista[Z]
        Z=Z+1
    Z=0
    while Z<len(lista):
        if lista[Z]==contador:
            cantidad=Z
            Z=len(lista)+1
        Z=Z+1
    if cantidad==0:
        nombre="Cetirizina"
    elif cantidad==1:
        nombre="Fexofenadina"
    elif cantidad==2:
        nombre="Loratadina"
    else:
        nombre="Desloratadina"
    print("------------------------------------------------------------------")
    print("El medicamento menos vendido es:",nombre, "con ",contador,"unidades")
    print("------------------------------------------------------------------")
    return 0

def promedio_de_ventas(lista):
    primera_lista=[]
    Z=0
    contador=0
    while Z<len(lista):
        contador=contador+lista[Z]
        Z=Z+1
    promedio=contador/4

    print("---------------------------------------------------------------------------")
    Z=0
    while Z<len(lista):
        if lista[Z]<promedio:
            if lista [Z]==0:
                print("Cetirizina a vendido:", lista[Z],"unidades y el promedio es:",promedio)
                print("---------------------------------------------------------------------------")
            elif lista [Z]==1:
                print("Fexofenadina a vendido:", lista[Z],"unidades y el promedio es:",promedio)
                print("---------------------------------------------------------------------------")
            elif lista [Z]==2:
                print("Loratadina a vendido:", lista[Z],"unidades y el promedio es:",promedio)
                print("---------------------------------------------------------------------------")
            else:
                print("Desloratadina a vendido:", lista[Z],"unidades y el promedio es:",promedio)
                print("---------------------------------------------------------------------------")
        Z=Z+1

def promedio_ventas_igual_superior(lista):
    primera_lista=[]
    Z=0
    contador=0
    while Z<len(lista):
        contador=contador+lista[Z]
        Z=Z+1
    promedio=contador/4

    Z=0
    while Z<len(lista):
        if lista[Z]<promedio:
            if lista [Z]==0:
                print("Cetirizina a vendido:", lista[Z],"unidades y el promedio es:",promedio)
                print("---------------------------------------------------------------------------")
            elif lista [Z]==1:
                print("Fexofenadina a vendido:", lista[Z],"unidades y el promedio es:",promedio)
                print("---------------------------------------------------------------------------")
            elif lista [Z]==2:
                print("Loratadina a vendido:", lista[Z],"unidades y el promedio es:",promedio)
                print("---------------------------------------------------------------------------")
            else:
                print("Desloratadina a vendido:", lista[Z],"unidades y el promedio es:",promedio)
                print("---------------------------------------------------------------------------")
        Z=Z+1

def venta(cantidad_vendidos):
    print("--------------------------------------------------")
    print("------- BIENVENIDO A FARMACIA MUNDO SANO ---------")
    print("--------------------------------------------------")
    print("|       Medicamento       |  Precio de Venta CLP |")
    print("--------------------------------------------------")
    print("|       Cetirizina        |      $14.999         |")
    print("|       Fexofenadina      |      $13.499         |")
    print("|       Loratadina        |      $5.500          |")
    print("|       Desloratadina     |      $8.390          |")
    print("--------------------------------------------------")
    print("Ingrese La cantidad de medicamentos que desea comprar (SI NO DESEA COMPRAR, INGRESE UN 0 RESPECTIVAMENTE)")
    
    x = 0
    while x==0:
        ceritizina=input("Ceritizina: ")
        validar_ceritizina=es_numerico(ceritizina)
        if validar_ceritizina==True:
            if int(ceritizina)>=0:
                cantidad_vendidos=Append_python(cantidad_vendidos,int(ceritizina),0)
                x=1
            else:
                print("-------------------------------------------")
                print("Porfavor ingrese un número entero positivo")
                print("-------------------------------------------")
        else:
            print("---------------------------")
            print("Porfavor ingrese un número")
            print("---------------------------")
    x=0
    while x==0:
        fexofenadina=input("Fexofenadina: ")
        velidar_fexofenadina=es_numerico(fexofenadina)
        if velidar_fexofenadina==True:
            if int(fexofenadina)>=0:
                cantidad_vendidos=Append_python(cantidad_vendidos,int(fexofenadina),1)
                x=1
            else:
                print("-------------------------------------------")
                print("Porfavor ingrese un número entero positivo")
                print("-------------------------------------------")
        else:
            print("---------------------------")
            print("Porfavor ingrese un número")
            print("---------------------------")
    x=0
    while x==0:
        loratadina=input("Loratadina: ")
        validar_loratadina=es_numerico(loratadina)
        if validar_loratadina==True:
            if int(loratadina)>=0:
                cantidad_vendidos=Append_python(cantidad_vendidos,int(loratadina),2)
                x=1
            else:
                print("-------------------------------------------")
                print("Porfavor ingrese un número entero positivo")
                print("-------------------------------------------")
        else:
            print("---------------------------")
            print("Porfavor ingrese un número")
            print("---------------------------")
    x=0
    while x==0:
        desloratadina=input("Desloratadina: ")
        validar_desloratadina=es_numerico(desloratadina)
        if validar_desloratadina==True:
            if int(desloratadina)>=0:
                cantidad_vendidos = Append_python(cantidad_vendidos,int(desloratadina),3)
                x=1
                os.system("cls")
            else:
                print("-------------------------------------------")
                print("Porfavor ingrese un número entero positivo")
                print("-------------------------------------------")
        else:
            print("---------------------------")
            print("Porfavor ingrese un número")
            print("---------------------------")
    return cantidad_vendidos

cant_vendidos=venta(cant_vendidos)

Z=True
while Z==True:
    print("¿QUE DESEA REALIZAR?")
    print("1) Mostrar la cantidad vendida de cada uno de los medicamentos")
    print("2) Mostrar el total (en CLP) por cada uno de los medicamentos")
    print("3) Mostrar el medicamento mas vendido")
    print("4) Mostrar el medicamento menos vendido")
    print("5) Mostrar el nombre de los medicamentos cuya cantidad de ventas sea menor al promedio de las cantidades vendidas")
    print("6) Mostrar el nombre de los medicamentos cuya cantidad de ventas sea igual o superior al promedio de las cantidades vendidas")
    print("7) Mostar el total general de ventas realizadas")
    print("8) Salir")
    print("Ingrese una de las opciones: ")
    opcion=input()
    validar_opcion=es_numerico(opcion)
    opcion=int(opcion)

    if validar_opcion==True:
        os.system("cls")
        if int(opcion)==1:
            cantidad_de_ventas(cant_vendidos)
        elif int(opcion)==2:
            total_de_ventas(cant_vendidos)
        elif int(opcion)==3:
            mas_vendido(cant_vendidos)
        elif int(opcion)==4:
            menos_vendido(cant_vendidos)
        elif int(opcion)==5:
            promedio_de_ventas(cant_vendidos)
        elif int(opcion)==6:
            promedio_ventas_igual_superior(cant_vendidos)
        elif int(opcion)==7:
            total_vendido(cant_vendidos)
        elif int(opcion)==8:
            print("GRACIAS POR SU COMPRA, HASTA LUEGO")
            Z=False
        else:
            print("--------------------------------------------")
            print("Porfavor ingrese un número dentro del rango")
            print("--------------------------------------------")
    else:
        print("-----------------------------------")
        print("Porfavor ingrese un valor numerico")
        print("-----------------------------------")
