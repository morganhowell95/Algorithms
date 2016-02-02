#Two Sum
#Caleb Kim

# Given an array of integers, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution.

# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ndx1 = -1
        ndx2 = -1
        dict = {}
        values = {}
        for ndx,value in enumerate(nums):
            dict[(ndx + 1, value)] = ndx + 1
            if value in values:
                values[value].append(ndx + 1)
            else:
                values[value] = [ndx + 1]
        for idx,val in enumerate(nums):
            ndx1 = idx + 1
            a = 0
            if len(values[val]) > 1:
                a = 1
            if target - val in values and (values[target - val][a], target - val) in dict:
                if a == 0 and target - val == val:
                    continue
                else:
                    ndx2 = dict[(values[target - val][a],target - val)]
                    return [ndx1, ndx2]
        return [ndx1, ndx2]