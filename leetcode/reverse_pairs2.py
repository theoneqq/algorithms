class solution:
    def merge(self, l, m, r):
        tmp = []
        nums = self.nums

        i, j = l, m + 1
        while i <= m or j <= r:
            if i > m:
                tmp.append(nums[j])
                j += 1
            elif j > r:
                tmp.append(nums[i])
                i += 1
            else:
                if nums[i] < nums[j]:
                    tmp.append(nums[i])
                    i += 1
                else:
                    tmp.append(nums[j])
                    j += 1
        nums[l:r+1] = tmp

    
    def helper(self, l, r):
        if l == r:
            return 0
        count = 0
        m = (l + r) // 2
        count += self.helper(l, m) + self.helper(m + 1, r)

        nums = self.nums
        i, j = l, m + 1
        while i <= m and j <= r:
            if nums[i] > 2 * nums[j]:
                count += m - i + 1
                j += 1
            else:
                i += 1
        self.merge(l, m, r)
        return count


    def reverse_pairs(self, nums):
        self.nums = nums
        return self.helper(0, len(nums) - 1)

print('result: {0}'.format(solution().reverse_pairs([1,3,2,3,1])))
print('result: {0}'.format(solution().reverse_pairs([2,4,3,5,1])))
print('result: {0}'.format(solution().reverse_pairs([3,1])))
print('result: {0}'.format(solution().reverse_pairs([1])))
print('result: {0}'.format(solution().reverse_pairs([0])))
