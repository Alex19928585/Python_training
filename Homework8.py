import os

# Task 1
print('***' * 50)
print('Task 1')
sum_of_int = 0
with open('index.txt') as file:
    for line in file:
        for num in line:
            if num.isdigit():
                sum_of_int += int(num)
print(f"Task 1. Сумма всех цифр равна {sum_of_int}")

# Task 2
print('***' * 50)
print('Task 2')
with open("index.txt") as file:
    reversed_line = file.read()
    reversed_line = reversed_line[::-1]
with open("reversed_data_file.txt", "w") as reversed_data_file:
    reversed_data_file.write(reversed_line)
print('Task 2 done')

# Task 3
print('***' * 50)
print('Task 3')
text = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. '''
with open("file_with_some_text.txt", "w") as file_with_some_text:
    file_with_some_text.write(text)
with open("file_with_some_text.txt") as file_with_some_text:
    text_in_file = file_with_some_text.read()
count = 0
vowels_letters = []
for letter in text_in_file.lower():
    if letter in 'aeiouy':
        count += 1
        vowels_letters.append(letter)
with open("file_with_vowels_letters.txt", 'w') as file_with_vowels_letters:
    file_with_vowels_letters.write(str(vowels_letters))
print(f'Количество гласных букв в тексте равна {count}')

# Task 4
print('***' * 50)
print('Task 4')
text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore 
magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo 
consequat. '''
with open("new_text_file.txt", "w") as new_text_file:
    new_text_file.write(text)
with open("new_python_file.py", 'w') as new_python_file:
    new_python_file.write(text)
text_file_size = os.path.getsize('new_text_file.txt')
python_file_size = os.path.getsize('new_python_file.py')
if text_file_size > python_file_size:
    print(f'Текстовый файл больше, чем Пайтон файл на {text_file_size - python_file_size} Bytes')
elif python_file_size > text_file_size:
    print(f'Пайтон файл больше чем Тестовый файл на {python_file_size - text_file_size} Bytes')
else:
    print(f'Размеры файлов равны и их размер {text_file_size} Bytes')
