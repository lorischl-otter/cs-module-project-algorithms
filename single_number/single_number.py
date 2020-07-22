'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
from collections import Counter


def single_number(arr):
    # user Counter to return last in the list (or least) \
    # of most common counts
    least = Counter(arr).most_common()[-1][0]
    return least


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")


# Understanding the problem:
# only one number in the list will appear just once
# need to figure eliminate the numbers that appear twice,
# and return numbers that appear only once (can assume wil always appear)
# should be able to have a O(1) solution

# Problem solving:
# Can we keep a count for each value?
# is there a builtin method for this?
# try Python's 'counter'
# need to index into the correct answer, first by indexing
# to the last of the list, and then indexing to just the number
