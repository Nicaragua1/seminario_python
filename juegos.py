import hangman
import reversegam
import tictactoeModificado
import json
import time
import PySimpleGUI as sg

def leerCampos():
    nombre = input('ingrese su nombre: ')
    edad   = input('ingrese su edad: ')
    hora  = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
    diccio = {}
    diccio['nombre'] = nombre
    diccio['edad'] = edad
    diccio['hora'] = hora
    return diccio

def actualizar_listado(listbox, lista):
	listbox.Update(map(lambda x: x, lista))	

sg.theme('Dark Blue 3')      ##########  INTERFAZ
layout = [  [sg.Text('Elegi cual juego queres jugar             ')],
            [sg.Button('Ahorcado')],
			[sg.Button('Otello')],
			[sg.Button('Ta-Te-Ti')],
			[sg.Text('Sesiones de hoy')],
			[sg.Listbox( values=[], key='historial', size= (60,10) )],
			[sg.Text('(El historial completo se guarda en DatosJugadores.txt)')],
			[ sg.Button('Salir')]]

window = sg.Window('Window Title', layout)
window.DisableClose = True
lista = []

while True:
	event, values = window.read()
	if event in (None, 'Ahorcado'): #click en boton ahorcado
		window.hide()        #escondo ventana
		datos = leerCampos() #ingreso datos del usuario
		hangman.main()	     #ejecuto juego
	if event in (None, 'Otello'):
		window.hide()
		datos = leerCampos()
		tictactoeModificado.main()	
	if event in (None, 'Ta-Te-Ti'):
		window.hide()
		datos = leerCampos() 
		reversegam.main()	
	if event in (None, 'Salir'):
		break   
	lista.append(datos) #cargo datos a lista cuando termina de jugar
	actualizar_listado(window.FindElement('historial'), lista) #agrego las sesiones
	window.un_hide()

archivo = open("DatosJugadores.txt", "w") #cargo el JSON
datoss = lista
json.dump(datoss, archivo)
archivo.close()
window.close()

archivo = open("DatosJugadores.txt", "r")  ## leo el JSON
datos = json.load(archivo)
print(json.dumps(datos,sort_keys=False, indent=4))
archivo.close()