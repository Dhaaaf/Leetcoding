# Did a mock interview over google doc today with my coach. Will give you the same question next time we pairboard. It was a pretty good one

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
