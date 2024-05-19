import random
user =  input('Введите то, что вы хотите показать (камень, ножницы или бумага): ')
possible_moves = ['камень', 'ножницы', 'бумага']
computer = random.choice(possible_moves)
print(f'\nВы выбрали {user}, компьютер выбрал {computer}. \n')


if user == computer:
    print('Ничья!')
elif user == 'камень':
    if computer == 'ножницы':
        print('Вы победили!')
    else:
        print('Вы проиграли!')
elif user == 'бумага':
    if computer == 'камень':
        print('Вы выиграли!')
    else:
        print('Вы проиграли!')
elif user == 'ножницы':
    if computer == 'бумага':
        print('Вы выиграли!')
    else:
        print('Вы проиграли!')
