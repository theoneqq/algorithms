class solution:
    def helper(self, idx1, idx2) -> int:
        dp_key = '{0}:{1}'.format(idx1, idx2)
        if dp_key in self.dps:
            return self.dps[dp_key]

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

        dp_value = min(cond1, cond2, cond3, cond4)
        self.dps[dp_key] = dp_value
        return dp_value

    def min_distance(self, word1, word2) -> int:
        self.word1 = word1
        self.word2 = word2
        self.dps = {}

        return self.helper(0, 0)

print('result: {0}'.format(solution().min_distance('intention', 'execution')))
