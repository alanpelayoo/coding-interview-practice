'''
combinacion_1 = []
combinacion_2 = []
combinaciones = []

numero = 264910
num_str = str(numero)

digitos_num = len(num_str)
for i in range(0,digitos_num):
	combinacion_1.append(num_str[i])
	

combinaciones.append(combinacion_1)
print(combinaciones)
'''

def combinacion_x(str_num):
	ln = len(str_num)
	if (ln ==1):
		print("1 dig")
	elif (ln ==2):
		print("2 dig")




numero = 1
stri_numero = str(numero)
combinacion_x(stri_numero)

