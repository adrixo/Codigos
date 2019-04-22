# -*- coding: utf-8 -*-

#Biblioteca para el manejo de matrices
import numpy as np
import itertools
import re

# dadas unas ecuaciones parametricas podemos obtener los vectores de la matriz asociada sustituyendo las coordenadas con una base
# input: parametricas (lista de listas):
#          la primera lista se corresponde con las variables a tomar en cuenta
#          las siguientes con las distintas ecuaciones parametricas de cada posicion
# output: vectores asociados (lista de listas) (matriz generadora)
def obtenerParametricas( parametricas, clase=2):
    vectores = []
    vectoresIndex = 0
    #   {x+z, x+z, y,2x,3y,4z} => [[x,y,z],'x+z','x+z','y','2*x','3*y','4*z']

    #1. se resuelve con la base (1,0,0), (0,1,0), (0,0,1)
    for var in parametricas[0]:
        vector = parametricas[1:]
        vectores.append([])
        for ecuacion in vector:
            for varIter in parametricas[0]:
                if varIter == var:
                    ecuacion = ecuacion.replace(varIter, '1')
                else:
                    ecuacion = ecuacion.replace(varIter, "0")
            resultadoEcuacion = eval(ecuacion)%clase
            vectores[vectoresIndex].append(resultadoEcuacion)
        vectoresIndex += 1

    # 2. se quitan vectores proporcionales
    # por ejemplo en: [['x','y','z','t','s'],'x+z+t','x+z+t','y+s','2*x+2*t','3*y+3*s','4*z']
    vectores = eliminarVectoresProporcionales(vectores, clase=2)

    return vectores

# Un vector es proporcional si se puede obtener como combinacion lineal de otros
# input: vectores(lista de listas)
#        clase
# output: vectores no proporcionales (lista de listas)
def eliminarVectoresProporcionales(vectores, clase=2):
    # 2. se quitan vectores proporcionales
    # por ejemplo en: [[1 1 0 0 0 0],[0 0 1 0 1 0], [1 1 0 0 0 0]
    vectorIndex = -1
    arrayPosicionesProporcionales = []
    for vector in vectores:
        vectorIndex += 1
        if sum(vector) == 0:
            arrayPosicionesProporcionales.append(vectorIndex)#si es el vector nulo
            continue

        #comparamos uno a uno los vectores
        vectorCompararIndex = -1
        for vectorComparar in vectores:
            vectorCompararIndex += 1
            if vectorIndex >= vectorCompararIndex: #ignoramos si son el mismo o ya fueron comparados
                continue

            #tenemos dos vectores siendo comparados
            proporcionales = True
            valor = 31416 #si coincide siempre, son proporcionales
            for i in range(len(vector)):
                if vectorComparar[i]==0: #evitar division por cero
                    if vector[i]==0:
                        continue
                    else:
                        proporcionales = False
                        break

                if vector[i] == 0:
                    proporcionales = False
                    break

                if valor == 31416:
                    valor = vector[i]/vectorComparar[i]
                else:
                    if valor != vector[i]/vectorComparar[i]:
                        proporcionales = False
                        break

            if proporcionales: #si son proporcionales el segundo desaparece
                arrayPosicionesProporcionales.append(vectorCompararIndex)

    for i in arrayPosicionesProporcionales[::-1]:
        vectores.pop(i)

    return vectores

#Corresponde con el numero de variables origen
def obtenerDimensionParametricas(parametricas):
    return len(parametricas[0])

#corresponde con el numero de ecuaciones
def obtenerLongitudParametricas(parametricas):
    return len(parametricas)-1

# definicion: La matriz generadora que contiene las columnas de la matriz identidad de tamaño k*k se dice que es una matriz generadora sistematica
# Esta funcion permite la manipulacion manual de la matriz
# input: matriz (np.matriz)
#        dimension del codigo
#        longitud del codigo
#        clase del codigo
#        nombre (string para informar)
#        tipoMatriz: 'generadora' o 'control'
# output: matriz sistematica o matriz modificada si se presiona x
def diagonalizacionManual(matriz, dimension, longitud, clase, nombre, tipoMatriz):

    if tipoMatriz == 'generadora':
        final = np.identity(dimension)
        parteSistematica = lambda matriz : matriz[:,:dimension]
    elif tipoMatriz == 'control':
        final = np.identity(longitud-dimension)
        parteSistematica = lambda matriz : matriz[longitud-(longitud-dimension):,:]
    else:
        print("Error Diagonalización manual")
        return matriz

    if (not np.array_equal(parteSistematica(matriz), final)):
        print("\nLa matriz "+tipoMatriz+" del codigo: "+nombre+" no es sistemática, requiere de manipulación manual para obtener la identidad a la izquierda:")
        print("Respetar los espacios. x para terminar.\n")

    while not np.array_equal(parteSistematica(matriz), final):
        print(matriz)
        print("\nIntroduce una operacion: ")
        print(" - suma: f1 = f1 -2 f2")
        print(" - intercambio filas: f1 = f2")
        print(" - intercambio columnas: c1 = c2")
        entrada = raw_input("->")

        if entrada == 'x':
            return matriz % clase

        patron = re.compile("(f\d = f\d [-|+|]\d* f\d|f\d = f\d$|c\d = c\d$)")
        if not patron.match(entrada):
            print("\n\n!!!!\nOperación incorrecta, respete los espacios.\n")
            continue


        if entrada.count('f')==2: #intercambio
            destino = int((entrada.split(" = "))[0].split("f")[1]) -1
            intercambio = int((entrada.split(" = "))[1].split("f")[1]) -1
            matriz = intercambiaFilas(matriz, destino, intercambio)

        if entrada.count('c')==2: #intercambio columnas
            destino = int((entrada.split(" = "))[0].split("c")[1]) -1
            intercambio = int((entrada.split(" = "))[1].split("c")[1]) -1
            matriz = intercambiaColumnas(matriz, destino, intercambio)

        if entrada.count('f')>2: #suma
            if entrada.split(" ")[3] == '-':
                operacion = -1
            elif entrada.split(" ")[3] == '+':
                operacion = 1
            else:
                operacion =  int(entrada.split(" ")[3])
            primero = int(entrada.split(" ")[2].split("f")[1]) -1
            segundo = int(entrada.split(" ")[4].split("f")[1]) -1
            matriz = sumaFilas(matriz, operacion, primero, segundo)

    return matriz % clase

#https://www.math.ubc.ca/~pwalls/math-python/linear-algebra/solving-linear-systems/
# Intercambia las filas i y j de la matriz
def intercambiaFilas(matriz, i, j):
    matriz[[i,j]] = matriz[[j,i]]
    return matriz

# Intercambia las columnas i y j de la matriz
def intercambiaColumnas(matriz, i, j):
    matriz=matriz.T
    matriz[[i,j]] = matriz[[j,i]]
    return matriz.T

# suma a la fila i la fila j*k
def sumaFilas(matriz, k, i, j):
    fila = matriz[[i]]
    sumando = matriz[[j]]
    fila = (fila + (sumando*k)) % 2
    matriz[[i]] = fila
    return matriz


#https://github.com/cryptogoth/skc-python/blob/master/skc/diagonalize.py
TOLERANCE2 = 1e-14
##############################################################################
# Diagonalize the given unitary in the given basis, returning the
# diagonal matrix W, and the unitary matrix V such that
#  V * U * V^{-1} = W
# Equivalently, you can call conjugate(W, V) to recover U
# from skc_group_factor
def diagonalize(matrix_U, basis):
	d = basis
	#print "U= " + str(matrix_U)

	(eig_vals, eig_vecs) = np.linalg.eig(matrix_U)

	#print "eig_vals= " + str(eig_vals)
	#print "eig_vecs= " + str(eig_vecs)

	eig_length = len(eig_vecs)
	assert(len(eig_vals) == eig_length)

	# Create the diagonalization matrix V
	matrix_V = np.matrix(eig_vecs) #numpy.matrix(rows)

	#print "V= " + str(matrix_V)

	# Get adjoint
	#matrix_V_dag = numpy.transpose(numpy.conjugate(matrix_V))

	# Eigenvector matrix should be unitary if we are to have
	# V dagger be the same as V inverse
	#assert_matrix_unitary(matrix_V, TOLERANCE6, message=str())


	# Multiply V^{-1} * U * V to diagonalize
	matrix_W = matrix_V.I * matrix_U * matrix_V

	# Assert that we can recover matrix U
	#matrix_U2 = matrix_V * matrix_W * matrix_V.I
	#assert_matrices_approx_equal(matrix_U, matrix_U2, trace_distance)

	#print "W= " + str(matrix_W)

	# Construct the diagonalized matrix that we want
	matrix_diag = np.matrix(np.eye(d), dtype=np.complex)
	for i in range(eig_length):
		matrix_diag[(i,i)] = eig_vals[i]

	# Verify that off-diagonal elements are close to zero
	for i in range(eig_length):
		for j in range(eig_length):
			if (i != j):
				assert_approx_equals(matrix_W[(i,j)], 0)

	for i in range(eig_length):
		assert_approx_equals(matrix_W[(i,i)], eig_vals[i])
        print(matrix_V, matrix_W)
	return (matrix_V, matrix_W)

##############################################################################
def assert_and_print(bool_condition, arg_to_stringify, msg_prefix=""):
	if (not bool_condition):
		print "[ASSERTION FAILED] " + msg_prefix + ": " + str(arg_to_stringify)
	assert(bool_condition)

##############################################################################
def assert_approx_equals_tolerance(value1, value2, tolerance, message=""):
	diff = abs(value1 - value2)
	assert_and_print(diff < tolerance, diff, message)

##############################################################################
def assert_approx_equals(value1, value2, message=""):
	assert_approx_equals_tolerance(value1, value2, TOLERANCE2, message)
