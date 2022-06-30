# task_1
print('task_1')

list_of_dif_objects = [1, 'a', True, 1.201, 'False', ['a'], (1, 2), '']

types = [type(obj) for obj in list_of_dif_objects]
print(*types)

# task_2
print('task_2')

list_of_objects = input('Введите различные элементы через пробел: ').split(' ')

for i in range(0, len(list_of_objects), 2):
    if i != len(list_of_objects) - 1:
        intermed = list_of_objects[i + 1]
        list_of_objects[i + 1] = list_of_objects[i]
        list_of_objects[i] = intermed

print(*list_of_objects)

# task_3
print('task_3')

month_number = int(input('Введите номер месяца: '))

seasons = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

for months in seasons:
    if month_number in seasons[months]:
        print(months)

# task_4
print('task_4')

string_in = input('Введите строку со словами через пробел: ').split(' ')

[print(f'{word_ind + 1}) {string_in[word_ind][0: 10]}') for word_ind in range(len(string_in))]

# task_5
print('task_5')

my_list = [7, 5, 3, 3, 2]

new_rate = int(input('Введите цифру: '))

my_list.append(new_rate)
print(sorted(my_list, reverse=True))

# task_6
print('task_6')

command = ''
count = 1
structure = []
while command != 'Стоп!':
    name = input('Введите название товара: ')
    price = int(input('Введите цену товара: '))
    quantity = int(input('Введите кол-во товара: '))
    un_of_meas = input('Введите единицу измерения товара: ')

    structure.append((count, {'название': name, 'цена': price, 'количество': quantity, 'eд': un_of_meas}))

    count += 1

    command = input('Введите "Стоп!" если закончили вводить товары: ')

analytics = {'название': [], 'цена': [], 'количество': [], 'eд': [structure[0][1]['eд']]}

for i in structure:
    for j in analytics:
        if j != 'eд':
            analytics[j].append(i[1][j])

print(analytics)
