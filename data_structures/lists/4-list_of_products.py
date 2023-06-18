def find_product(lst):
    prod = []
    left = 1
    for num in lst:
        prod.append(left)
        left*=num
    print(prod)
    right = 1
    for idx in range(len(lst)-1, -1, -1):
        prod[idx] = prod[idx] * right
        right *= lst[idx]  

    return prod

print(find_product([1, 2, 3, 4]))