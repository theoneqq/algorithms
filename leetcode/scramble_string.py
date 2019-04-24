class solution:
    def __init__(self):
        self.dp = {}

    def is_scramble(self, s1, s2) -> bool:
        if (s1, s2) in self.dp:
            return self.dp[(s1, s2)]

        res = False
        s_len = len(s1)
        if s_len < 2:
            res = s1 == s2
            self.dp[(s1, s2)] = res
            return res

        for i in range(1, s_len):
            if self.is_scramble(s1[:i], s2[:i]) and self.is_scramble(s1[i:], s2[i:]):
                res = True
                break
            if self.is_scramble(s1[:i], s2[-i:]) and self.is_scramble(s1[i:], s2[:-i]):
                res = True
                break

        self.dp[(s1, s2)] = res
        return res

print('result: {0}'.format(solution().is_scramble('abcdefghijklmnopq', 'efghijklmnopqcadb')))
print('result: {0}'.format(solution().is_scramble('great', 'rgeat')))
