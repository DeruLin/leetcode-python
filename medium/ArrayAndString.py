def lengthOfLongestSubstring(s):
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


def longestPalindrome(s):
    longest_palindrome = ""
    longest_length = 0
    length = len(s)
    reverse_s = s[::-1]
    i, j = 0, 0
    while i < length:
        temp_i = i
        j = 0
        while j < length:
            if s[temp_i] != reverse_s[j]:
                j += 1
            else:
                while temp_i < length and j < length and s[temp_i] == reverse_s[j]:
                    temp_i += 1
                    j += 1


if __name__ == "__main__":
    print(longestPalindrome("aab"))
