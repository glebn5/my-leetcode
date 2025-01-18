class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        ans = ''
        if letters[-1] <= target:
            return letters[0]
        else:
            for letter in letters:
                if letter > target:
                    ans += letter
                    break

        return ans