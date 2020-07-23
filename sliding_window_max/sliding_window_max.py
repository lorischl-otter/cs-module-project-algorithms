'''
Input: a List of integers as well as an integer `k` representing the size
of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # create an empty max_values list
    max_values = []
    # for loop, to pass through entire array, looking at indices i + k
    for i, i_value in enumerate(nums[0:-k+1]):
        max_values.append(max(nums[i:i+k]))
 
    return max_values


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

# Understanding the problem:
# need to be able to 'slide a window' of length k over an array,
# then return the max value for that window
# should be able to optimize to O(n)

# Problem solving:
# Main problem to tackle is the 'window' 
# then from there, should be easy to find the max of each & append to list