# -*- coding: utf-8 -*-


# Cesar: Sumar constante a cada simbolo
# f: k -> k
#    m -> m + clave
def caesarCrypt(mensaje, clavePrivada):
    menor = ord('a')
    mayor = ord('z')
    tamcuerpo = mayor-menor + 1
    encriptado = ""

    for i in range(len(mensaje)):
        encriptado = encriptado + chr( (((ord(mensaje[i]) - menor) + clavePrivada) % tamcuerpo) + menor)

    return encriptado

def caesarDecrypt(mensaje, clavePrivada):
    menor = ord('a')
    mayor = ord('z')
    tamcuerpo = mayor-menor + 1
    encriptado = ""

    for i in range(len(mensaje)):
        encriptado = encriptado + chr( (((ord(mensaje[i]) - menor) - clavePrivada) % tamcuerpo) + menor)

    return encriptado


def aplicacionAfin(mensaje, claveprivada, constante)
