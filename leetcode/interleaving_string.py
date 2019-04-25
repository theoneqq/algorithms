class solution:
    def helper(self, idx1, idx2, idx3) -> bool:
        if (idx1, idx2, idx3) in self.dp:
            return self.dp[(idx1, idx2, idx3)]

        res = False
        s1, s2, s3 = self.s1, self.s2, self.s3
        if idx3 >= len(s3):
            res = True
        elif idx1 >= len(s1) and idx2 >= len(s2):
            res = idx3 >= len(s3)
        else:
            if idx1 < len(s1):
                res = res or self.helper(idx1 + 1, idx2, idx3)
                if s1[idx1:idx1 + 1] == s3[idx3:idx3 + 1]:
                    res = res or self.helper(idx1 + 1, idx2, idx3 + 1)
            if idx2 < len(s2):
                res = res or self.helper(idx1, idx2 + 1, idx3)
                if s2[idx2:idx2 + 1] == s3[idx3:idx3 + 1]:
                    res = res or self.helper(idx1, idx2 + 1, idx3 + 1)

        self.dp[(idx1, idx2, idx3)] = res
        return res

    def is_interleave(self, s1, s2, s3) -> bool:
        self.dp = {}
        self.s1, self.s2, self.s3 = s1, s2, s3

        return self.helper(0, 0, 0)

print('result: {0}'.format(solution().is_interleave('', '', '')))
