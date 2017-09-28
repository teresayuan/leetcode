# LeetCode - strStr
#
# Find needle in haystack
#
# Returns the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
#
# Solution is O(n*m), n = length of haystack, m = length of needle
# checking window in haystack is O(m) and it is checked O(n) times

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1

if __name__ == '__main__':
    # needle = 'his'
    needle = 'hi'
    haystack = 'heyhibyeseeya'
    sol = Solution().strStr(haystack, needle)
    print(sol)
