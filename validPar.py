# LeetCode 7. Reverse Integer
# 8/19/17 - accepted
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid
# but "(]" and "([)]" are not.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        dict = {')':'(', ']':'[', '}':'{'}
        stack = []

        for c in s:
            if c in dict.values():
                stack.append(c)
            elif c in dict.keys():
                if len(stack) == 0 or dict[c] != stack.pop():
                    return False

        return len(stack) == 0

if __name__ == '__main__':
    x = '(){'
    sol = Solution().isValid(x)
    print(sol)