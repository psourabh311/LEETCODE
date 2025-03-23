class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = 0
        original = x
        while x > 0:
            y = y * 10 + (x % 10)
            x = x // 10

        if original == y:
            return True
        else:
            return False
