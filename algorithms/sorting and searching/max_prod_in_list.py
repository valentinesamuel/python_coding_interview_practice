from decimal import Decimal


def max_product_of_two(lst):
    max1 = lst[0]
    max2 = Decimal('-Infinity')

    min1 = lst[0]
    min2 = Decimal('-Infinity')

    for num in lst:
        if num >= max1:
            max2 = max1
            max1 = num
        elif num > max2 and num < max1:
            max2 = num

        if num <= min1:
            min2 = min1
            min1 = num
        elif num > min2 and num < min1:
            min2 = num

    return max(max1 * max2, min1 * min2)


numbers = [-10, -5, 2, 8, 12]
result = max_product_of_two(numbers)
print("Maximum product:", result)
