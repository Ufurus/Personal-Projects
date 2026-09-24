# x = 121
x = -121

class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = (str(x) == str(x)[::-1])
        return a

testing_solution = Solution()
print(testing_solution.isPalindrome(x))
