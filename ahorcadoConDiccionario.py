import random

def definicion_palabras():
	palabras = {1:['gato', 'perro','pato','elefante','lobo'], 2:['rojo','azul','verde','amarillo'], 3:['milanesa','pure','pizza','salchicha']}
	return palabras

def definicion_ahorcado():	
	ahorcado = [' O ', '/|\\','/ \\']
	return ahorcado

def eleccion_de_tema():
	tema = int(input('Elige un tema:\n 1: animales\n 2: colores\n 3: comidas\n '))
	return tema

def eleccion_de_palabra(palabras, tema):
	pal = palabras[tema][random.randrange(len(palabras[tema]))]
	return pal

def separar_palabra(pal):
	pal_separada = []
	for y in pal:
		pal_separada.append(['_ '])
	return pal_separada

def mostrar_lineas(pal):
	print ('- '*len(pal))

def jugar(pal, pal_separada, ahorcado):
	cantidad_letras_adivinadas = 0
	cantidad_partes_cuerpo = 0
	sigue = True
	while sigue:
		letra = input('Ingresa una letra: ').lower()
		if letra in pal:		
			for pos in range(len (pal)):			
				if pal[pos] == letra:
					pal_separada[pos] = letra				
					cantidad_letras_adivinadas = cantidad_letras_adivinadas + 1
			
			pal_imprime = ''
			for y in pal_separada:
				pal_imprime = pal_imprime + y[0]
			print (pal_imprime)
			if cantidad_letras_adivinadas == len(pal):
				print ('Ganaste')
				sigue = False
		
		else:
			cantidad_partes_cuerpo=cantidad_partes_cuerpo + 1
			for x in range(cantidad_partes_cuerpo):
				print (ahorcado[x])
			if cantidad_partes_cuerpo == 3:
				print ('Perdiste!. La palabra era:', pal)
				sigue = False
jugar_de_nuevo = 'si'
while jugar_de_nuevo == 'si':
	palabras = definicion_palabras
	ahorcado = definicion_ahorcado
	tema = eleccion_de_tema
	pal = eleccion_de_palabra(palabras, tema)
	pal_separada = separar_palabra(pal)
	mostrar_lineas(pal)
	jugar(pal, pal_separada, ahorcado)
	print('Seguimos jugando? (si o no)')
	jugar_de_nuevo = input()		
		
		
		
			
	
