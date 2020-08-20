'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    left = [0] * len(arr)
    right = [0] * len(arr)
    out = []
    # Do left side of index
    left[0] = 1
    for x in range(1, len(arr)):
        left[x] = arr[x - 1] * left[x - 1]
    # Do right side of index
    right[-1] = 1
    for x in range(len(arr)-1)[::-1]:
        right[x] = arr[x + 1] * right[x + 1]
    # Setup final array
    for x in range(len(arr)):
        out.append(left[x] * right[x])

    return out


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
