
def remove_even(lst):

    """
    for every item in the list, check the remainder using 2. If the remainder is not 0, then that number is an odd
    number because 2 is an even number and ite can divide any even number without remainder
    """

    if len(lst) == 0:
        return lst
    if lst == None:
        return 
    if not isinstance(lst, list):
        raise TypeError('Invalid data type. Please input a list')

    result = []
    for idx in range(len(lst)):
        # print(lst[idx])
        if lst[idx] % 2 != 0:
            result.append(lst[idx])
    return(result)

lst = [20, 36, -139, 12, -31, 168, -66, -36, 151, -132, 30, -17, -179, 133, -91, 61, -112, 23, 77, 53, -64, 81, 191, 8, -40, 163, -107, 29, -56, -121, -63, 45]

print(remove_even(lst), end='\n 👇\n')
print([-139, -31, 151, -17, -179, 133, -91, 61, 23, 77, 53, 81, 191, 163, -107, 29, -121, -63, 45])
