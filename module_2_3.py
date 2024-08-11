my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
Zero = 0
while Zero <= len(my_list):
    if my_list[Zero] > 0 and my_list[Zero] != 0:
        print(my_list[Zero])
        Zero += 1
    elif my_list[Zero] == 0:
        Zero += 1
        continue
    else:
        break
