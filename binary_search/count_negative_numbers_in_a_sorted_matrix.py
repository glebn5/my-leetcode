def countNegatives(grid: list[list[int]]) -> int:
    count = 0
    for num in grid:
        low = 0
        high = len(num) - 1
        for n in num:
            if n < 0:
                count += 1
    #     while low <= high:
    #         mid = (low + high) // 2
    #         guess = num[mid]
    #         if guess < 0:
    #             count += high - 1
    #             print(count, high)
    #             high = mid - 1
    #         else:
    #             low = mid + 1
    #         print('-----')
    return count

print(countNegatives([[-1, -2, -3], [-4, -5, -6],[-7, -8, -9]]))