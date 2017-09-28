# LeetCode - Longest Common Prefix
#
# Find the longest common prefix among an array of strings
# Vertical Scanning solution

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if strs == None or len(strs) == 0:
            return ''

        for i in range(0, len(strs[0])):
            c = strs[0][i]

            for j in range(1, len(strs)):
                # later string is shorter than first string or character mismatch
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][0:i]

        return strs[0]

if __name__ == '__main__':
    # x = ['leets', 'leetcode', 'leet', 'leeds']
    # x = ['a', 'b', 'c', 'd']
    x = ['be', 'beee', 'beeds', 'beer']
    sol = Solution().longestCommonPrefix(x)
    print(sol)
