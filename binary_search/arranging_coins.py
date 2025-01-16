def arrangeCoins(n: int) -> int:
    low = 1
    high = n
    c = 0
    while low <= high:
        mid = (low+high)//2
        coins = ((mid/2)*(mid+1))
        if coins > n:
            high = mid -1
        else:
            low = mid + 1
            c = max(mid, c)
    return c
        
    
print(arrangeCoins(8))
