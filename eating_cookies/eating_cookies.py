'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Base Cases
    if n <= 1:
        # Eat 1
        return 1
    elif n == 2:
        # Eat 1+1 & 2
        return 2
    # elif n == 3:
    #     # Eat 1+2, 1+1+1, 2+1, & 3
    #     return 4
    # Recurse the three possibilities
    elif n >= 3:
        return (eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3))

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
