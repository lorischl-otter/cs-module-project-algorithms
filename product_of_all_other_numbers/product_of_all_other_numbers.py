'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    # Your code here
    new = []
    for i, value_i in enumerate(arr):
        new_val = 1
        for j, value_j in enumerate(arr):
            new_val *= value_j
        new.append(new_val / value_i)
    return new

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

# Understanding the problem:
# must multiply each value by all other values in the list,
# and return a list of those values
# should be able to optimize to O(n)
