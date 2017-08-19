# LeetCode 9. Palindrome Number
# 8/19/17 - accepted
# Determine whether an integer is a palindrome. Do this without extra space.


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        if x < 10:
            return True

        num = str(x)

        for i in range(0, len(num)/2):
            if num[i] != num[len(num)-i-1]:
                return False

        return True



s = Solution()
sol = s.isPalindrome(12321)

print sol