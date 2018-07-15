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

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map = {}
        for num in nums:
            temp = map.get(num, 0)
            map[num] = temp + 1
        sort_map = sorted(map.items(), key=lambda item: item[1], reverse=True)
        result = []
        count = 0
        for l in sort_map:
            if count >= k:
                break
            result.append(l[0])
            count += 1
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2))
