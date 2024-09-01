def print_params(a=1, b="Строка", c=True):
    print(a, b, c)

print_params(1,2,3)
print_params(1,2)
#print_params(1,2,3,4, False)  Не работает!
print_params()
print_params(b = 25) # Работает
print_params(c = [1,2,3]) # Работает

values_list_ = [False, [25, 16], 13.5]
values_dict_ = {"a": 55, "b": False, "c": "Stroka"}

print_params(*values_list_)
print_params(**values_dict_)

values_list_2 = [[17, 29], "Hz"]
print_params(*values_list_2, 42) # Работает
