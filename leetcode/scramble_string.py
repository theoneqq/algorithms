class solution:
    def __init__(self):
        self.dp = {}

    def is_scramble(self, s1, s2) -> bool:
        comb = s1 + s2
        if comb in self.dp:
            return self.dp[comb]

        res = False
        s_len = len(s1)
        if s_len < 2:
            res = s1 == s2
            self.dp[comb] = res
            return res

        for i in range(1, s_len):
            s1_left, s1_right = s1[:i], s1[i:]
            s2_left1, s2_right1 = s2[:i], s2[i:]
            if self.is_scramble(s1_left, s2_left1) and self.is_scramble(s1_right, s2_right1):
                res = True
                break
            if i != (s_len >> 1):
                s2_left2, s2_right2 = s2[-i:], s2[:-i]
                if self.is_scramble(s1_left, s2_left2) and self.is_scramble(s1_right, s2_right2):
                    res = True
                    break

        self.dp[comb] = res
        return res

print('result: {0}'.format(solution().is_scramble('abcdefghijklmnopq', 'efghijklmnopqcadb')))
print('result: {0}'.format(solution().is_scramble('abcd', 'cadb')))
