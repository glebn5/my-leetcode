from math import ceil

def minEatingSpeed(piles: list[int], h: int) -> int:
    low = 1
    high = max(piles)
    res = high
    while low <= high:
        hours = 0
        k = (low+high)//2
        for p in piles:
            hours += ceil(p/k)
        if hours <= h:
            res = k
            high = k - 1
        else:
            low = k + 1
    return res


print(minEatingSpeed([3,6,7,11], 8))
