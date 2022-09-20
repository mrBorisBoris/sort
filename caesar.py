alphabet = [x for x in 'абвгдежзийклмнопрстуфхцчшщъыьэюя']
message = input('Введите сообщение: ')
message = list(message)
shift = int(input('Введите сдвиг: '))

index_letter = 0
swap_letter = ''
swapped_word = ''


for letter in message:
    if letter != ' ':
        swap_letter = letter
        index_letter = alphabet.index(swap_letter)
        swap_letter = alphabet[(index_letter + shift) % len(alphabet)]
        swapped_word += swap_letter
    elif letter == '.':
        swapped_word += '.'
    else:
        swapped_word += ' '

swapped_word = list(swapped_word)

swapped_string = ''

print('Зашифрованное сообщение:', swapped_string.join(swapped_word))
