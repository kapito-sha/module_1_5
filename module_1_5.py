immutable_var = ([1, 2, 5.84], True, 1422, 'pretty', 13.5)
print('изначальный кортеж:', immutable_var)
# Кортеж - неизменяемый объект, значения его элементов изменить нельзя
# Но можно изменить значение внутри списка в составе кортежа
immutable_var[0][0] = 'fantastic'
print('измененный кортеж:', immutable_var)
mutable_list = [564, 42.5, 'kitty', False]
print('изначальный список:', mutable_list)
mutable_list[1] = 0.2
print('измененный список:', mutable_list)

