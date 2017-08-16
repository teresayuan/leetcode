# LeetCode 1. Two Sum
# 8/11/17 - accepted

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):

                if nums[i] + nums[j] == target:
                    return [i, j]

        return -1

a = Solution()
sol = a.twoSum([-3,4,3,90], 0)

print sol