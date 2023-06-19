def find_minimum(arr):
    # Write your code here
    curr_min = arr[0]
    for num in arr:
        if num < curr_min:
            curr_min = num
    
    return curr_min

print(find_minimum([100, 12, 34, 40]))
print(find_minimum([4, 5, 0, 3, 6]))