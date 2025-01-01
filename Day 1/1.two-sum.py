#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
# O(n^2)


# @lc code=start
class Solution(object):
    def twoSum( nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                #print(i,j)
                if nums[j] == target - nums[i]:
                    return [i,j]
            return []
    #print(twoSum(nums=[2,7,11,15],target=9))       
# @lc code=end

