# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numeros[-4])

# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]
# resultado = list1 + list2
# print(resultado)
# print(resultado[4::-2])

# b1 = True
# b2 = True
# b3 = False
# b4 = b1 and b2 and (not b3)
# print(f'b4 {b4}')

# name = input('What is your name?: ')
# age = int(input(f'How old are you? {name}: '))
# has_license = input(f'Do you have license? {name} ') == 'yes'
# has_insurance = input(f'Do you have insurance? {name} ') == 'yes'

# if age >= 18 and has_license and has_insurance:
#     print('meets all the requirements for the job')
# elif age >= 18 and has_license and not has_insurance:
#     print('Under review')
# else:
#     print('You do not meet the job requirements')

import platform
print(platform.python_version())
