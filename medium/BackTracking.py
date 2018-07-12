class Solution:

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        num_to_letters = {2: ["a", "b", "c"], 3: ["d", "e", "f"],
                          4: ["g", "h", "i"], 5: ["j", "k", "l"], 6: ["m", "n", "o"],
                          7: ["p", "q", "r", "s"], 8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]}
        letters_list = []
        for num in digits:
            letters_list.append(num_to_letters[int(num)])
        size = len(letters_list)
        if size == 0:
            return result
        elif size == 1:
            return letters_list[0]
        else:
            return self.get(letters_list, 0, size)

    def get(self, letters_list, current, size):
        result = []
        if current < size - 1:
            for letter in letters_list[current]:
                for s in self.get(letters_list, current + 1, size):
                    result.append(letter + s)
        elif current == size - 1:
            for letter in letters_list[current]:
                result.append(letter)
        return result

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        elif n == 1:
            return ["()"]
        else:
            return list(self.generate(1, n))

    def generate(self, count, n):
        temp_set = set()
        if count == n:
            temp_set.add("()")
            return temp_set
        else:
            pre_set = self.generate(count + 1, n)
            for s in pre_set:
                for i in range(len(s) + 1):
                    s_list = list(s)
                    s_list.insert(i, "()")
                    temp_set.add("".join(s_list))
        return temp_set

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [[nums[0]]]
        else:
            result = []
            for num in nums:
                nums_copy = nums.copy()
                nums_copy.remove(num)
                sub_permute = self.permute(nums_copy)
                for permute in sub_permute:
                    permute.append(num)
                    result.append(permute)
            return result

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        result = [[]]
        result.extend([[i] for i in nums])
        for i in range(2, length + 1):
            result.extend(self.get_subset(i, nums))
        return result

    def get_subset(self, n, nums):
        if n == 1:
            return [[i] for i in nums]
        else:
            result = []
            for i in range(len(nums) - 1):
                for temp_set in self.get_subset(n - 1, nums[i + 1:len(nums)]):
                    temp_set.append(nums[i])
                    result.append(temp_set)
            return result

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return False
        row_len = len(board)
        if row_len == 0:
            return 0
        col_len = len(board[0])
        letter = word[0]
        indexes = []
        for i in range(row_len):
            for j in range(col_len):
                if letter == board[i][j]:
                    indexes.append((i, j))
        result = False
        for index in indexes:
            result = result or self.visit(index, word[1:len(word)], board)
            if result:
                return True
        return False

    def visit(self, pre_index, word, board):
        if len(word) == 0:
            return True
        else:
            letter = word[0]
            i = pre_index[0]
            j = pre_index[1]
            tmp = board[i][j]  # first character is found, check the remaining part
            board[i][j] = "#"  # avoid visit agian
            row_len = len(board)
            col_len = len(board[0])
            if j + 1 < col_len and board[i][j + 1] == letter \
                    and self.visit((i, j + 1), word[1:], board):
                return True
            if i + 1 < row_len and board[i + 1][j] == letter \
                    and self.visit((i + 1, j), word[1:], board):
                return True
            if i - 1 >= 0 and board[i - 1][j] == letter \
                    and self.visit((i - 1, j), word[1:], board):
                return True
            if j - 1 >= 0 and board[i][j - 1] == letter \
                    and self.visit((i, j - 1), word[1:], board):
                return True
            board[i][j] = tmp
            return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.exist([["a", "b"]], "ba"))
