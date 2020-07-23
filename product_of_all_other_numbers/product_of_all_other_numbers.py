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
    output = product_of_all_other_numbers(arr)

    print(f"Output of product_of_all_other_numbers: {output}")

# Understanding the problem:
# must multiply each value by all other values in the list,
# and return a list of those values
# should be able to optimize to O(n)
