#
# @lc app=leetcode id=27 lang=python
#
# [27] Remove Element
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == val:
                nums.pop(i)
        print(nums)
        return len(nums)
# @lc code=end

