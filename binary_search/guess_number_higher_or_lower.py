class Solution:
    def guessNumber(self, n: int) -> int:
        low = 0
        high = n
        while low <= high:
            mid = (low + high) // 2
            num = guess(mid)
            if num == -1:
                high = mid - 1
            elif num == 1:
                low = mid + 1
            else:
                return mid
