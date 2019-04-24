class solution:
    def is_scramble(self, s1, s2) -> bool:
        s_len = len(s1)
        if s_len < 2:
            return s1 == s2

        for i in range(1, s_len - 1):
            s1_left, s1_right = s1[0:i], s1[i:-1]
            s2_left1, s2_right1 = s2[0:i], s2[i:-1]
            s2_left2, s2_right2 = s2_right1, s2_left1
            if (self.is_scramble(s1_left, s2_left1) and self.is_scramble(s1_right, s2_right1)) or (self.is_scramble(s1_left, s2_left2) and self.is_scramble(s1_right, s2_right2)):
                return True

        return False


print('result: {0}'.format(solution().is_scramble('r', 's')))
