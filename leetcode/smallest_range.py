class solution():
    def smallest_range(self, nums) ->[]:
        nl = len(nums)
        idxs = [ 0 for i in range(nl) ]
        left, right = min([ nums[i][0] for i in range(nl) ]), max([ nums[i][-1] for i in range(nl) ])
        d = right - left

        while idxs != [ len(l) - 1 for l in nums ]:
            curs = [ nums[i][idxs[i]] for i in range(nl) ]
            curs_copy = curs.copy()
            curs.sort()

            cur_min, cur_max = curs[0], curs[-1]
            if cur_max - cur_min < d or (cur_max - cur_min == d and cur_min < left):
                left, right, d = cur_min, cur_max, cur_max - cur_min

            for cur in curs:
                idx = curs_copy.index(cur)
                if idxs[idx] + 1 < len(nums[idx]):
                    idxs[idx] += 1
                    break
        return [left, right]


ls = [[1, 9, 15, 24, 36], [0, 9, 12, 40], [-5, 18, 22, 30]]
print('result: {0}'.format(solution().smallest_range(ls)))
