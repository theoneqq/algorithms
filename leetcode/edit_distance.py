class solution:
    def helper(self, idx1, idx2) -> int:
        if idx1 >= len(self.word1):
            return len(self.word2) - idx2
        if idx2 >= len(self.word2):
            return len(self.word1) - idx1

        cond1 = 1 + self.helper(idx1 + 1, idx2)
        cond2 = 1 + self.helper(idx1, idx2 + 1)
        cond3 = max(len(self.word1), len(self.word2))
        if self.word1[idx1:idx1 + 1] == self.word2[idx2:idx2 + 1]:
            cond3 = self.helper(idx1 + 1, idx2 + 1)
        cond4 = 1 + self.helper(idx1 + 1, idx2 + 1)

        return min(cond1, cond2, cond3, cond4)

    def min_distance(self, word1, word2) -> int:
        self.word1 = word1
        self.word2 = word2

        return self.helper(0, 0)

print('result: {0}'.format(solution().min_distance('inten', '')))
