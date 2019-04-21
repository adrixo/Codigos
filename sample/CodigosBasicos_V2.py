#!/usr/bin/python
# Programa para el testeo del objeto Codigo
# Se generan 3 codigos diferentes y se imprimen sus caracteristicas

from Codigo import *
import Parametricas as p


i = 'a'
while i != 'x':
    print("\n\tEste programa presenta los codigos:\n\t - triple repeticion\n\t - triple control\n\t - paridad\n")
    print("Se pueden cargar desde: \n 1. Ecuaciones parametricas\n 2. Matrices Generadoras\n 3. Matrices de Control\n 4. Salir")
    try:
        i = str(input("-> "))
    except:
        continue

    if i == '1':
        TR = Codigo(2, parametricas=p.triple_repeticion, nombre="triple repeticion")
        TC = Codigo(2, parametricas=p.triple_control, nombre="Triple control")
        P = Codigo(2, parametricas=p.paridad, nombre="Paridad")

    elif i == '2':
        TR = Codigo(2, generadora='TripleRepeticion_Generadora.txt', nombre="triple repeticion")
        TC = Codigo(2, generadora='TripleControl_Generadora.txt', nombre="Triple control")
        P = Codigo(2, generadora='Paridad_Generadora.txt', nombre="Paridad")

    elif i == '3':
        TR = Codigo(2, control='TripleRepeticion_Control.txt', nombre="triple repeticion")
        TC = Codigo(2, control='TripleControl_Control.txt', nombre="Triple control")
        P = Codigo(2, control='Paridad_Control.txt', nombre="Paridad")

    elif i == '4':
        break

    else:
        print("Opcion incorrecta\n")
        continue

    codigos = [TR, TC, P]

    for c in codigos:
        if c.M > 17:
            # En caso de haber muchas palabras no las imprimimos
            c.imprimirInformacionCodigo(G=True, H=True)
        else:
            c.imprimirInformacionCodigo(G=True, H=True, dic=True, sin=True)
        try:
            input("<Enter para siguiente>")
        except:
            continue
