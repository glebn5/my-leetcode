def mySqrt(x: int) -> int:
    low = 0
    high = x
    while low <= high:
        mid = (low + high) // 2
        if mid**2 == x:
            return mid
        elif mid**2 > x:
            high = mid - 1
        else:
            low = mid + 1
    return high

print(mySqrt(1835651042))