print('*' * 50)
# Task № 1
print('Enumerate')
grocery = {'bread', 'milk', 'butter'}
enumerateGrocery = enumerate(grocery)
print(type(enumerateGrocery))
# converting to set
print(set(enumerateGrocery))
# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(set(enumerateGrocery))

grocery = {'bread', 'milk', 'butter'}
for item in enumerate(grocery):
    print(item)

print('\n')
for count, item in enumerate(grocery):
    print(count, item)

print('\n')
# changing default start value
for count, item in enumerate(grocery, 100):
    print(count, item)


print('*' * 50)
print('Task with max()')
number = {3, 2, 8, 5, 10, 6}
largest_number = max(number)
print("The largest number is:", largest_number)

languages = {"Python", "C Programming", "Java", "JavaScript"}
largest_string = max(languages)
print("The largest string is:", largest_string)

print('*' * 50)
print('Task with min()')
number = {3, 2, 8, 5, 10, 6}
smallest_number = min(number)
print("The smallest number is:", smallest_number)

languages = {"Python", "C Programming", "Java", "JavaScript"}
smallest_string = min(languages)
print("The smallest string is:", smallest_string)

print('*' * 50)
print('Task with sorted()')
py_set = {'e', 'a', 'u', 'o', 'i'}
print('Отсортированные данные можем вывести только в виде списка, т.к. преобразовав в Сет данные будут неупорядочены',
      sorted(py_set))

py_set = {'e', 'a', 'u', 'o', 'i'}
print(sorted(py_set, reverse=True))


def take_second(elem):
    return elem[1]


# random set
random = {(2, 2), (3, 4), (4, 1), (1, 3)}

# sort set with key
sorted_list = sorted(random, key=take_second)
sorted_set = set(sorted_list)
# print set
print('Sorted set:', sorted_set)


participant_set = {
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
}


def sorter(item):
    # Since highest marks first, least error = most marks
    error = 100 - item[1]
    age = item[2]
    return (error, age)


sorted_set = set(sorted(participant_set, key=sorter))
print(sorted_set)

participant_set = {
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
}

sorted_set = set(sorted(participant_set, key=lambda item: (100-item[1], item[2])))
print(sorted_set)

print('*' * 50)
print('Task with sum()')
numbers = {2.5, 3, 4, -5}
# start parameter is not provided
numbers_sum = sum(numbers)
print(numbers_sum)
# start = 10
numbers_sum = sum(numbers, 10)
print(numbers_sum)

print('*' * 50)
# Task № 2
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set3 = {3, 4, 6, 7}
set4 = set1.intersection(set2, set3)
print('Task 2, intersection =', set4)

print('*' * 50)
# Task № 3
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set3 = {3, 4, 6, 7}
set4 = set1.difference(set2, set3)
print('Task 3, difference = ', set4)

print('*' * 50)
# Task № 4
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set3 = {3, 4, 6, 7}
set4 = set1.union(set2, set3)
print('Task 4, union =', set4)

print('*' * 50)
# Task № 5
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
sampleSet.update(sampleList)
print('Task 5, update = ', sampleSet)

print('*' * 50)
# Task № 6
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.intersection(set2)
print('Task 6', set3)

print('*' * 50)
# Task № 7
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.union(set2)
print('Task 7', set3)

print('*' * 50)
# Task № 8
set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1.difference_update(set2)
print('Task 8', set1)

print('*' * 50)
# Task № 9
set1 = {10, 20, 30, 40, 50}
set1.discard(10)
set1.discard(20)
set1.discard(30)
print('Task 9', set1)

print('*' * 50)
# Task № 10
print('Task 10')

print('*' * 50)
# Task № 11
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
set3 = set1.intersection(set2)
print('Task 11', set3)

print('*' * 50)
# Task № 12
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
set1.update(set2)
print('Task 12', set1)

print('*' * 50)
# Task № 13
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection_update(set2)
print('Task 13', set1)
