# // Given an array of arrays where the inner array represents a server's uptime. Each element representing 1 hr.

# // Server will always start true or reset true.

# // Return an array of arrays where the inner arrays have server uptime ratio.

# // eg

# // input: [ [true, true, true, false, false, false], [true, false], [true, true, false] ]
# // output: [ [0.50], [0.50], [0.67] ]

def server_uptime_ratio(servers):
    res = []
    for s in servers:
        length = len(s)
        left, right = 0, length - 1

        while left < right:
            mid = (left + right) // 2
            if s[mid] == False:
                right = mid
            if s[mid] == True:
                left = mid + 1

        ratio = left / length
        res.append(round(ratio, 2))

    return res
