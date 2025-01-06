#
# @lc app=leetcode id=258 lang=python
#
# [258] Add Digits
#

# @lc code=start
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = list(map(int, str(num)))

        if len(a) == 1:
            return a[0]

        while len(a) > 1:
            cnt = sum(a)
            a.clear()
            a = list(map(int,str(cnt)))

        return cnt
        
# @lc code=end

