# LeetCode 7. Reverse Integer
# 8/19/17 - accepted
# Reverse digits of an integer.
# Example1: x = 123, return 321
# Example2: x = -123, return -321
# The input is assumed to be a 32-bit signed integer. Your function should
# return 0 when the reversed integer overflows.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        neg = False

        if x < 0:
            neg = True
            x = -x

        num = str(x)
        rev = ''

        for i in range(0, len(num)):
            rev += num[len(num)-i-1]

        rev_num = int(rev)

        # limit of int is (2^31)-1 aka 2,147,483,647, return 0 if overflow
        if abs(rev_num) > ((2**31)-1):
            return 0

        if neg:
            return -rev_num

        return rev_num

if __name__ == '__main__':
    x = 1563847412
    sol = Solution().reverse(x)
    print(sol)