class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1
        x = 0
        while x < j + 1:
            if nums[x] == 0:
                nums[x] = nums[i]
                nums[i] = 0
                i += 1
                x += 1
            elif nums[x] == 2:
                nums[x] = nums[j]
                nums[j] = 2
                j -= 1
            else:
                x += 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.sortColors([0, 2, 1]))
