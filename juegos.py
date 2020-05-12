import hangman
import reversegam
import tictactoe
import json # uso el modulo json porque solo almaceno datos que sean de tipo string, ademas por la ventaja que tiene de que de que interactua con otras aplicaciones que no sean de python
def main(args):
	datos={'nombre':[],'juegos':[]} # eligi la estructura de un diccionario con 2 llaves que almacenen valores de tipo lista para que en una llave se almacene los datos del jugador y en la tra llave los juegos que jugo
	arch=open('jugadores.txt','a')
	nombre=input('ingresa tu nombre: ')
	datos['nombre'].append(nombre)
	sigo_jugando = True
	while sigo_jugando:
		print('''
		Elegí con qué juego querés jugar:
		1.- Ahorcado
		2.- Ta-TE-TI
		3.- Otello
		4.- Salir''')
		opcion = input()
		if opcion == '1':
			hangman.main()
			datos['juegos'].append('hangman')
		elif opcion == '2':
			tictactoe.main()
			datos['juegos'].append('tictactoe')
		elif opcion == '3':
			reversegam.main()
			datos['juegos'].append('reversegam')
		elif opcion == '4':
			sigo_jugando = False
	json.dump(datos,arch)
	arch.close()	
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
