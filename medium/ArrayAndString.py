class Solution:
    def lengthOfLongestSubstring(self, s):
        max_len = 0
        max_str = ""
        i = 0
        j = 1
        str_len = len(s)
        if str_len == 1 or str_len == 0:
            return str_len
        else:
            my_set = set(s[i])
            while j < str_len:
                before_len = len(my_set)
                my_set.add(s[j])
                if before_len == len(my_set):
                    if j - i > max_len:
                        max_len = j - i
                        max_str = s[i:j]
                    my_set.clear()
                    for x in range(i, j):
                        if s[x] == s[j]:
                            i = x + 1
                            break
                    my_set = set(s[i:j])
                else:
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        max_str = s[i:j + 1]
                    j += 1
        if i == 0:
            return s
        else:
            return max_str

    # 更好的算法是马拉车算法
    def longestPalindrome(self, s):
        longest_str = ""

        length = len(s)
        if length <= 1:
            return s
        for i in range(length):
            temp1 = self.helper(s, i, i)
            temp2 = self.helper(s, i, i + 1)
            if len(temp1) > len(temp2) and len(temp1) > len(longest_str):
                longest_str = temp1
            if len(temp1) < len(temp2) and len(temp2) > len(longest_str):
                longest_str = temp2
        return longest_str

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        small_val = 0
        big_val = 0
        start = 1
        for i in range(1, length):
            if nums[i] - nums[i - 1] > 0:
                small_val = nums[i - 1]
                big_val = nums[i]
                start = i
                break
        for i in range(start, length):
            if small_val < big_val < nums[i]:
                return True
            if small_val < nums[i] < big_val:
                big_val = nums[i]
            if nums[i] - nums[i - 1] > 0 and nums[i] < big_val:
                small_val = nums[i - 1]
                big_val = nums[i]
        return False


if __name__ == "__main__":
    nums = [5,1,5,5,2,5,4]
    print(Solution().increasingTriplet(nums))
