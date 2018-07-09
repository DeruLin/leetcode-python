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


if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(3))
