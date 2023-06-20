def find_first_unique(lst):
    register = {}
    for num in lst:
        if num not in register:
            register[num] = 1
        else:
            value = register.get(num, 1)
            register[num] = value+1
    for key in register.keys():
        if register[key] == 1:
            return key


