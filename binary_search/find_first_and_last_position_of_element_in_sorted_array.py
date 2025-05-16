def searchRange(nums, target: int):
    result = []
    result.append(searchLeftIndex(nums, target))
    result.append(searchRightIndex(nums, target))
    return result

def searchLeftIndex(nums, target):
    result = -1
    left = 0
    right = len(nums)-1
    while left<=right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

def searchRightIndex(nums, target):
    result = -1
    left = 0
    right = len(nums)-1
    while left<=right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

print(searchRange([5,7,7,8,8,10], 8))
print(searchRange([5,7,7,8,8,10], 6))
print(searchRange([1], 1))