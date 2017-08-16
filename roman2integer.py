# LeetCode 13. Roman to Integer
# 8/15/17 - Accepted
# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        convert = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        total = convert[s[0]]
        for i in range(1, len(s)):
            prev_num = convert[s[i-1]]
            num = convert[s[i]]

            if prev_num < num:
                total += num - 2*prev_num
            else:
                total += num

        return total

s = Solution()
sol = s.romanToInt('XXVI')

print sol