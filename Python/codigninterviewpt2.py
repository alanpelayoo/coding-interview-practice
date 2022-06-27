
''' Facebook Coding Interview Problems
	by Alan Pelayo 10-08-21
	The following code works as an interpreter/decoder 
	where the user inputs a number, and the program
	determines the no. of possibilites to interprate
	that number with code following the corresponding 
	solution
'''

import string

def generar_lista():
	our_abs = list(string.ascii_lowercase)           
	rangos = enumerate(our_abs)
	return rangos

def estado_x(valor):
	if (valor<11):
		return estado_1(valor)
	
	elif (10<valor<100):
		return estado_2(valor)
	else:
		return estado_3()

def estado_1(numero_1):
	
	if (numero_1 ==0):
		return 0,None
	
	num_soluciones1 = 1

	lista_1 = generar_lista()
	
	for indix, letra in lista_1:
		indice = indix+1
		
		if indice == numero_1:

			return num_soluciones1,letra

			
			



	



def estado_2(numero_2):
	
	flag = True
	string_1 = str(numero_2)
	soluciones = []
	solucion_1 = []
	solucion_2 = []
	num_soluciones2 = 0

	valores_dun = []
	for x in string_1:
		valores_dun.append(int(x))
			

		
	for num_sep in valores_dun:

		a,b= estado_1(num_sep)
		if b== None:
			flag = False


		solucion_2.append(b)

	if flag:
		soluciones.append(solucion_2)
		num_soluciones2 =1 

		 
	'''En las lineas de cod anterior separamos los 2 digitos, en 2 numeros de uno y proponemos
	la solucion 2, que siempre sera la de los numeros separados.'''


	if (numero_2<27):
		num_soluciones2 = num_soluciones2+1
		f,h = estado_1(numero_2)
		solucion_1.append(h)

		soluciones.append(solucion_1)

		return num_soluciones2,soluciones
	else:
		return num_soluciones2,soluciones
		





def estado_3():

	return 3,'a'



num_solutions,letra = estado_x(55)
h = [letra]


print(num_solutions,letra)