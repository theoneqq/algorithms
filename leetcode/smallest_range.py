class solution():
    def smallest_range(self, nums) ->[]:
        nl = len(nums)
        idxs = [ 0 for i in range(nl) ]
        left, right = min([ nums[i][-1] for i in range(nl) ]), max([ nums[i][-1] for i in range(nl) ])
        d = right - left

        while idxs != [ len(l) - 1 for l in nums ]:
            curs = [ nums[i][idxs[i]] for i in range(nl) ]
            curs_copy = curs.copy()
            curs.sort()

            cur_min, cur_max = curs[0], curs[-1]
            if cur_max - cur_min < d or (cur_max - cur_min == d and cur_min < left):
                left, right, d = cur_min, cur_max, cur_max - cur_min

            for cur in curs:
                find = False
                for idx in range(len(curs_copy)):
                    if curs_copy[idx] == cur:
                        if idxs[idx] + 1 < len(nums[idx]):
                            find = True
                            idxs[idx] += 1
                            break
                if find:
                    break



        return [left, right]


#ls = [[1, 9, 15, 24, 36], [0, 9, 12, 40], [-5, 18, 22, 30]]
#ls = [[-5,-4,-3,-2,-1,1], [1,2,3,4,5]]
ls = [[1,3,5,7,9,10], [2,4,6,8,10]]
print('result: {0}'.format(solution().smallest_range(ls)))
