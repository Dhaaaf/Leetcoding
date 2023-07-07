# Given a range of integers, determine how many numbers have no repeating digits.

# Example:
# n = 80
# m = 120

# The lower and upper bounds are inclusive, so there are 120-79 = 41 values int he range. 

# There are 27 numbers with no repeating digits and 14 other numbers in the range. print 27

# countNumbers has the following parameter(s):
# int arr[q][2]: integer pairs representing inclusive lower(n) and upper (m) range limits.

# Print for each pair arr[i], print the number of integers in the inclusive rnage that qualify. There is no value to return from the function

## Solution that times out:
def count_numbers(ranges):
    for n, m in ranges:
        count = 0
        for num in range(n, m + 1):
            if len(str(num)) == len(set(str(num))):
                count += 1
        print(count)

# Test the function
ranges = [[80, 120], [10, 20]]
count_numbers(ranges)


## Solution that doesn't time out:
def count_numbers(ranges):
    # Lookup table
    lookup = [0] * 10001
    for num in range(1, 10001):
        if len(set(str(num))) == len(str(num)):
            lookup[num] = lookup[num-1] + 1
        else:
            lookup[num] = lookup[num-1]

    # Answer for each range
    for n, m in ranges:
        print(lookup[m] - lookup[n-1] if n > 0 else lookup[m])

# Test the function
ranges = [[80, 120], [10, 20]]
count_numbers(ranges)
