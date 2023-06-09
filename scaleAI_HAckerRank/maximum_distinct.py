# Consider 2 arrays a and b where each consists of n integers. In one operation:

# 1. Select two indices I and j (0, <, i,j <n)
# 2. Swap integers a[i) and b[j]

# This operation can be performed at lost k times.

# Find the maximum number of distinct elements that can be achieved in array a after at most k operations



# 10 / 15 solution
from collections import Counter
def getMaximumDistinctCount(a, b, k):
    # Write your code here
    freq_a = Counter(a)
    freq_b = Counter(b)

    for i in range(len(a)):
        for j in range(len(b)):
            if b[j] not in freq_a and k> 0:
                if freq_a[a[i]] > 1:
                    freq_a[a[i]] -= 1
                    a[i] = b[j]
                    freq_a[b[j]] = 1
                    k -= 1

    return len(freq_a)