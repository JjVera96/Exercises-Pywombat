if __name__ == '__main__':
	nums = { 
	1: 'Uno',
	2: 'Dos',
	3: 'Tres',
	4: 'Cuatro',
	5: 'Cinco',
	6: 'Seis',
	7: 'Siete',
	8: 'Ocho',
	9: 'Nueve',
	}
	singular = '{} elefante se balanceaba sobre la tela de una araña,\ncomo veía que resistía fue a buscar a otro elefante\n'
	plural = '{} elefantes se balanceaban sobre la tela de una araña,\ncomo veían que resistía fue a buscar a otro elefante\n'
	num = int(input('Repetir: '))

	for i in range(1,num+1):
		print(singular.format(i)) if i == 1 else print(plural.format(i))



