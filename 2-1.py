def dishes(number, cook_book, quantity_2):
	with open('recipes.txt', encoding='utf-8') as f:
			for line in f:
				dish = line.strip().lower()
				cook_book[dish]=number
				number+=1
				quantity = int(f.readline())
				quantity_2.append(str(quantity)) 
				for i in range(0,quantity):
					f.readline()
				f.readline()
			return(cook_book, quantity_2)


def compositions(composition):
	with open('recipes.txt', encoding='utf-8') as f:
		for line in f:
			quantity = int(f.readline())
			for i in range(0,quantity):
				composition.append(f.readline().strip('\n'))
			f.readline()
		return(composition)

def chosen_compositions(name, first, second, person, cook_book, quantity_2, composition):
	for dish, number in cook_book.items():
		if dish == name and int(number) == 0:
			second += int(quantity_2[0])
			for i in range(0, second):
				composition[i].split('|')
				print('{} {} {}'.format(composition[i].split('|')[0], person*int(composition[i].split('|')[1]), composition[i].split('|')[2]))
		elif dish== name and int(number) != 0:
			for m in range(int(number)):
				first += int(quantity_2[m])
			second = first+int(quantity_2[m+1])
			for i in range(first, second):
				composition[i].split('|')
				print('{} {} {}'.format(composition[i].split('|')[0], person*int(composition[i].split('|')[1]), composition[i].split('|')[2]))
	print()


def program():
	number = 0
	cook_book = {}
	quantity_2 = []
	composition = []
	dishes(number, cook_book, quantity_2)
	compositions(composition)
	name = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
	person = int(input('Введите количество человек: '))
	first = 0
	second = 0
	for i in range(len(name)):
		print('Блюдо: ', name[i])
		chosen_compositions(name[i], first, second, person, cook_book, quantity_2, composition)
	program()

program()

