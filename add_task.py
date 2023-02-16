# Даны числа a и b
# Выяснить, какое из них больше, не применяя операторов сравнения

set_a = set(i for i in range(int(input('Input a: '))))
set_b = set(i for i in range(int(input('Input b: '))))
flag1 = bool(set_a.difference(set_a.intersection(set_b)))
flag2 = 1-flag1
while flag1:
    print(f'Max = {a}')
    flag1 = False
while flag2:
    print(f'Max = {b}')
    flag2 = False


# list_check = [i for i in range(int(input('Input a: ')))]
# set_check = set(list_check)
# set_check.add(int(input('Input b: ')))

# bool_check_b = len(set_check) - len(list_check)
# bool_check_a = 1-bool_check_b

# while bool_check_b:
#     print(f'Max = {b}')
#     bool_check_b = False
# while bool_check_a:
#     print(f'Max = {a}')
#     bool_check_a = False




