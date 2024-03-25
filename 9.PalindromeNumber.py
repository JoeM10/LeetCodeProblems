# Original Solution.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringx = str(x)
        for index in range(len(stringx)):
            if stringx[index] != stringx[-index - 1]:
                return False
        return True

# Fast solution.
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         strx = str(x)
#         return strx == strx[::-1]