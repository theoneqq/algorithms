class solution:
    def find_min(self, nums) -> int:
        def helper(l, r):
            if r - l <= 1:
                return min(nums[l], nums[r])
            else:
                m = (l + r) // 2
                l_ok = nums[l] <= nums[m]
                r_ok = nums[m + 1] <= nums[r]
                if l_ok and r_ok:
                    return min(helper(l, m), helper(m + 1, r))
                elif not l_ok:
                    return helper(l, m)
                else:
                    return helper(m + 1, r)
        if len(nums) == 1:
            return nums[0]
        else:
            return helper(0, len(nums) - 1)
print('result: {0}'.format(solution().find_min([1,3,5])))
print('result: {0}'.format(solution().find_min([4,5,6,7,0,1,2])))
print('result: {0}'.format(solution().find_min([2,2,2,0,1])))
print('result: {0}'.format(solution().find_min([3,1])))
print('result: {0}'.format(solution().find_min([1,1])))
print('result: {0}'.format(solution().find_min([1,3])))
print('result: {0}'.format(solution().find_min([3,3,3])))
print('result: {0}'.format(solution().find_min([3,3,2])))
print('result: {0}'.format(solution().find_min([10,1,10,10,10])))
