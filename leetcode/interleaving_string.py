class solution:
    def helper(self, idx1, idx2, idx3) -> bool:
        if (idx1, idx2, idx3) in self.dp:
            return self.dp[(idx1, idx2, idx3)]

        res = False
        s1, s2, s3 = self.s1, self.s2, self.s3
        if idx1 >= len(s1):
            res = s2[idx2:] == s3[idx3:]
        elif idx2 >= len(s2):
            res = s1[idx1:] == s3[idx3:]
        else:
            if s1[idx1:idx1 + 1] == s3[idx3:idx3 + 1]:
                res = res or self.helper(idx1 + 1, idx2, idx3 + 1)
            if s2[idx2:idx2 + 1] == s3[idx3:idx3 + 1]:
                res = res or self.helper(idx1, idx2 + 1, idx3 + 1)

        self.dp[(idx1, idx2, idx3)] = res
        return res

    def is_interleave(self, s1, s2, s3) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        self.dp = {}
        self.s1, self.s2, self.s3 = s1, s2, s3

        return self.helper(0, 0, 0)

print('result: {0}'.format(solution().is_interleave('a', '', 'a')))
