def countNegatives(grid: list[list[int]]) -> int:
    count = 0
    for row in grid:
        low, high = 0, len(row) - 1
        while low <= high:
            mid = (low + high) // 2
            if row[mid] < 0:
                high = mid - 1
            else:
                low = mid + 1
        
        count += len(row) - low
    return count






# def countNegatives(grid) -> int:
#     count = 0
#     for arr in grid:
#         arr.sort()
#         for i in arr:
#             if i < 0:
#                 count += 1
#             else:
#                 break
#     return count

print(countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))