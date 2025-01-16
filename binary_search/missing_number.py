def missingNumber(nums: list[int]) -> int:
    nums.sort()
    
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Если значение по индексу mid совпадает с mid,
        # значит пропущенное число находится справа
        if nums[mid] == mid:
            left = mid + 1
        else:
            right = mid - 1
            
    # После выхода из цикла, left указывает на пропущенное число
    return left



print(missingNumber([0,1])) 
