# LeetCode - Remove Duplicates from Sorted Array
# 8/19/17 - accepted
# Given a sorted array, remove the duplicates in place such that each
# element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this in place
# with constant memory.
# For example,
# Given input array nums = [1,1,2], Your function should return length = 2,
# with the first two elements of nums being 1 and 2 respectively. It doesn't
# matter what you leave beyond the new length.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        curr = nums[0]
        i = 1

        while i < len(nums):
            if curr == nums[i]:
                del nums[i]
                continue
            else:
                curr = nums[i]
                i += 1
                if i == len(nums):
                    break

        return len(nums)

if __name__ == '__main__':
    x = []
    sol = Solution().removeDuplicates(x)
    print(sol)