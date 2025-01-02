#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x <0):
            return False
        rev = str(x)[::-1]
        
        if(x == int(rev)):
            return True
        
# @lc code=end

