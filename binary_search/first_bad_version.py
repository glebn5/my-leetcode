def firstBadVersion(n: int) -> int:
    low = 1
    high = n
    while low <= high:
        mid = (low + high) // 2
        if not(isBadVersion(mid)):
            low = mid + 1
        else:
            high = mid - 1
    return low