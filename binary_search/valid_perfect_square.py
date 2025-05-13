def isPerfectSquare(num: int) -> bool:
    left = 0
    right = num
    while left <= right:
        mid = (left+right)//2
        if mid**2 > num:
            right = mid - 1
        elif mid ** 2 < num:
            left = mid + 1
        else:
            return True
    return False
    

print(isPerfectSquare(16))