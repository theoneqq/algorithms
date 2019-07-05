class solution:
    def find(self, nums, nums_size, new_num, insert):
        insert_idx, count = 0, 0
        if nums_size > 0:
            if new_num < nums[0]:
                insert_idx, count = 0, nums_size
            elif new_num >= nums[-1]:
                insert_idx, count = nums_size, 0
            else:
                l, h = 0, nums_size - 1
                while h - l > 1:
                    mid = (l + h) // 2
                    if nums[mid] < new_num:
                        l = mid
                    else:
                        h = mid
                insert_idx = l - 1
                if new_num >= nums[l] and new_num < nums[h]:
                    insert_idx = l + 1
                elif new_num >= nums[h]:
                    insert_idx = h + 1
                count = nums_size - insert_idx
        if insert:
            nums.insert(insert_idx, new_num)
        return count

    def reverse_pairs(self, nums):
        count = 0
        tmp_nums = []
        for i in range(len(nums)):
            count += self.find(tmp_nums, i, nums[i] << 1, False)
            self.find(tmp_nums, i, nums[i], True)
        return count

print('result: {0}'.format(solution().reverse_pairs([1])))
print('result: {0}'.format(solution().reverse_pairs([])))
print('result: {0}'.format(solution().reverse_pairs([3,1])))
print('result: {0}'.format(solution().reverse_pairs([2,1])))
print('result: {0}'.format(solution().reverse_pairs([1,2,3,4,5])))
print('result: {0}'.format(solution().reverse_pairs([0,7,3,1,0,1])))
