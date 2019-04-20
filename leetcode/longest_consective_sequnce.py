class solution:
    def longest_consecutive(self, nums) -> int:
        d = {}
        for num in nums:
            if num in d:
                continue
            d[num] = [num, num]
            left, right = num - 1, num + 1
            if left in d and right in d:
                max_left, max_right = d[left][0], d[right][1]
                d[max_left][1] = max_right
                d[max_right][0] = max_left
            elif left in d:
                max_left = d[left][0]
                d[max_left][1] = num
                d[num][0] = left
            elif right in d:
                max_right = d[right][1]
                d[max_right][0] = num
                d[num][1] = right
        max_d = max(d.values(), key = lambda p: p[1] - p[0])
        return max_d[1] - max_d[0] + 1

print('result: {0}'.format(solution().longest_consecutive([0, -1, 2, 4, 1, 1, 5, 3])))
