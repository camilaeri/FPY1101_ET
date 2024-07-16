#librerias
import random
import csv
import os
clean="cls"
#listas y matrices
matriz_principal=[["NOMBRE", "SUELDO"]]
sueldos=[]
trabajadores=["Juan Perez", "Marìa Garcia", "Carlos Lopez", "Ana Martìnez",
                "Pedro Rodriguez", "Laura Hernandez", "Miguel Sanchez", "Isabel Gomez",
                "Francisco Diaz", "Elena Fernandez"]
matriz_reporte=[["NOMBRE", "SUELDO", "DESCUENTO SALUD", "DECUENTO AFP", "SUELDO LIQUIDO"]]
#funcion para asignar sueldos aleatorios entre 300000 y 2500000
def asignar_sueldos():
    for trabajador in trabajadores:
        sueldo=random.randint(300000, 2500000)
        matriz_principal.append([trabajador, sueldo])
    print("Los sueldos han sido asignados aleatoriamente a los trabajadores con exito")
#funcion para clasificar sueldos
def clasificar_sueldos():
    #si no se han asignado sueldos
    if not  matriz_principal[1:]:
        print("Aun no se han asignado sueldos a los trabajadores, por favor, primero asignelos")
    #si los sueldos ya fueron asignados
    else:
            #creamos matrices para contener los sueldos segun clasificacion
            sueldos_menores=[["NOMBRE","SUELDO"]]
            sueldos_intermedios=[["NOMBRE", "SUELDO"]]
            sueldos_mayores=[["NOMBRE", "SUELDO"]]
            #iniciamos contadores para contar la cantidad de sueldos dentro del rango
            cont_menor=0
            cont_intermedio=0
            cont_mayor=0
            #usamos for para iterar sobre la matriz principal
            for fila in matriz_principal[1:]:#nos saltamos el encabezado de la matriz
                nombre, sueldo=fila
                sueldos.append(sueldo)
                #clasificamos segun rango, aumentando contadores y agregando las filas a la matriz correspondiente
                if sueldo <800000:
                    cont_menor+=1
                    sueldos_menores.append(fila)
                elif sueldo >=800000 and sueldo <=2000000:
                    cont_intermedio+=1
                    sueldos_intermedios.append(fila)
                elif sueldo >2000000:
                    cont_mayor+=1
                    sueldos_mayores.append(fila)
            #sueldos menores a $800.000
            print(f"Sueldos menores a $800.000 TOTAL: {cont_menor}")
            print("")
            for fila in sueldos_menores:
                print(f"{fila[0]:<15} {fila[1]:<15}")
            #Sueldos entre $800.000 y $2.000.000
            print("")
            print(f"Sueldos entre $800.000 y $2.000.000 TOTAL: {cont_intermedio}")
            print("")
            for fila in sueldos_intermedios:
                print(f"{fila[0]:<15} {fila[1]:<15}")
            #sueldos superiores a $2.000.000
            print("")
            print(f"Sueldos superiores a $2.000.000 TOTAL: {cont_mayor}")
            print("")
            for fila in sueldos_mayores:
                print(f"{fila[0]:<15} {fila[1]:<15}")
            print("")
            #sumamos el total de los sueldos 
            total_sueldos=sum(sueldos)
            print(f"TOTAL SUELDOS ${total_sueldos}")
            return nombre
    #funcion para ver estadisticas
def ver_estadisticas():
    #si no se han asignado sueldos
    if not sueldos:
        print("Aun no se han asignado sueldos a los trabajadores, por favor asignelos primero")
    #si los sueldos ya fueron asignados.    
    else: 
        #calculamos las estadisticas
        sueldo_bajo=min(sueldos)
        sueldo_alto=max(sueldos)
        promedio_sueldo=sum(sueldos)/len(sueldos)
        producto=1
        for valor in sueldos:
            producto*=valor
        media_geometrica=producto**(1/len(sueldos))
        #mostramos las estadisticas
        print(f"El sueldo mas alto es: ${sueldo_alto}")
        print(f"El sueldo mas bajo es: ${sueldo_bajo}")
        print(f"El promedio de sueldos es: ${promedio_sueldo}")
        print(f"La media geometrica es:{media_geometrica}")
#funcion para reporte de sueldos
def reporte_sueldos():
    #si no se han asignado sueldos
    if not  matriz_principal[1:]:
        print("Aun no se han asignado sueldos a los trabajadores, por favor asignelos primero")
    #si los sueldos ya fueron asignados
    else:
        #recorremos la matriz que contiene nombre y sueldo
        for fila in matriz_principal[1:]:#nos saltamos el encabezado
            nombre, sueldo=fila
            #calculamos los descuentos
            desc_salud=round(sueldo*0.07)
            desc_afp=round(sueldo*0.12)
            sueldo_liquido=sueldo-desc_salud-desc_afp
            #agregamos cada calculo a la matriz del reporte
            matriz_reporte.append([nombre, sueldo, desc_salud, desc_afp, sueldo_liquido])
        #recorremos la matriz para imprimirla
        print("REPORTE DE SUELDOS")
        print("")
        for fila in matriz_reporte:
            print(f"{fila[0]:<18}  {fila[1]:<15}  {fila[2]:<15}  {fila[3]:<18}  {fila[4]:<15}")
        #guardamos la matriz en archivo csv
        with open ("reporte.csv", "w", newline="") as archivo_csv:
            escritor_csv=csv.writer(archivo_csv)
            escritor_csv.writerow(matriz_reporte)
        print("")
        print("El reporte de los sueldos a sido guardado en un archivo .csv con el nombre: reporte.csv")   
#funcion para salir del programa
def salir_programa():
    print("Finalizando programa...")
    print("Desarrollado por Camila Erices Ponce")
    print("RUT: 18.976247-K")

#menu principal
otra_accion=1
while otra_accion==1:
    print("Bienvenido, seleccione la opción que desea: ")
    print("1. Asignar Sueldos")
    print("2. Clasificar Sueldos")
    print("3. Ver Estadisticas")
    print("4. Reporte De Sueldos")
    print("5. Salir Del Programa")
    opcion_ok=True
    while opcion_ok==True:
        try: 
            opcion=int(input("Opción 1-5: "))
            os.system(clean)
            if opcion==1:
                asignar_sueldos()
                opcion_ok=False
            elif opcion==2:
                clasificar_sueldos()
                opcion_ok=False
            elif opcion==3:
                ver_estadisticas()
                opcion_ok=False
            elif opcion==4:
                reporte_sueldos()
                opcion_ok=False
            elif opcion==5:
                salir_programa()
                otra_accion_ok=False
                otra_accion=2
                break                
            else:
                print("Opcion invalida, seleccione 1-5")
        except ValueError:
            print("Opción invalida, seleccione 1-5")
    if opcion==5:
        break
    print("")
    print("Desea realizar otra accion? 1=si 2=no")
    otra_accion_ok=True
    while otra_accion_ok==True:
        try: 
            otra_accion=int(input("Opcion 1-2: "))
            if otra_accion==1:
                os.system(clean)
                otra_accion_ok=False          
            elif otra_accion==2:
                print("Programa finalizado")
                break
            else:
                print("Opcion invalida, seleccione 1-2 ")
        except ValueError:
            print("Opción invalida, seleccione 1-2")
   

    
        


    
