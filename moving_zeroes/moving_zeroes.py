'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    for x in arr:
        if x == 0:
            arr.remove(0)
            arr.append(0)
    return arr

    # Failed attempt -- did not work bc modified indices during for loop
    # for i, val in enumerate(arr):
    #     if val == 0:
    #         arr.pop(i)
    #         arr.append(val)
    # return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]
    arr = [0, 0, 0, 0, 3, 2, 1]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

# Understanding the problem:
# need to move all the zeros to the right of the integer
# return the same list
# should be able to optimize to O(1)
