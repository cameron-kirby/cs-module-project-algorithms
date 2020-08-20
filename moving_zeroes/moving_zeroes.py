'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Go through array
    for x in range(len(arr)):
        # If the item is not zero, move it to the front
        if arr[x] != 0:
            non_zero = arr.pop(x)
            arr.insert(0, non_zero)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")