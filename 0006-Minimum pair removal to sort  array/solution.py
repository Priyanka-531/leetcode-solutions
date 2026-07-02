class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def sorted_array(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True

        operations = 0

        while not sorted_array(nums):
            min_sum = float('inf')
            idx = 0

            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < min_sum:
                    min_sum = nums[i] + nums[i + 1]
                    idx = i

            nums = nums[:idx] + [nums[idx] + nums[idx + 1]] + nums[idx + 2:]
            operations += 1

        return operations
