'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。
示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
'''

class Solution:
    def searchRange(self, nums, target):
        # if target not in nums:
        #     return [-1,-1]

        i, j = 0, len(nums)-1
        while i <= j:
            if nums[i] < target:
                i += 1
            if nums[j] > target:
                j -= 1

            if nums[i] == nums[j]:
                pass

        if nums[i] == nums[j] and nums[i] == target:
            return [i, j]
        else:
            return [-1, -1]

    def searchRange_2(self, nums, target):

        j = len(nums)-1
        for i in range(len(nums)):
            if nums[i] == target:
                while j >= i and nums[j] != target:
                    j -= 1
                if nums[j] == target:
                    return [i,j]
                else:
                    return [-1,-1]
        return [-1,-1]


s = Solution()
nums = []
target = 7
print(s.searchRange_2(nums, target))
