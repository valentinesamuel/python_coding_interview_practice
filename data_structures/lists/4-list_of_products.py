def find_product(lst):
    product = []
    left = 1
    for num in lst:
        product.append(left)
        left *= num
    
    right = 1
    for idx in range(len(lst)-1, -1, -1):
        product[idx] = product[idx] * right
        right *= lst[idx]
    
    return product

print(find_product([2, 5, 9, 3, 6]))