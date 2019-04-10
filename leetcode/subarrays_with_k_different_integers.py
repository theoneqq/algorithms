class solution:
    def get_len(self, a: {}) -> int:
        count = 0
        for num in a:
            if a[num] > 0:
                count += 1
        return count


    def subarray_with_k_distinct(self, a: [int], k: int) -> int:
        count = 0
        counts = {}
        list_len = len(a)

        l = 0
        m = 0
        r = 0
        while l <= r and r < list_len:
            cur = a[r]
            counts[cur] = counts.get(cur, 0) + 1
            counts_len = self.get_len(counts)
            print('counts', counts)
            if self.get_len(counts) > k:
                while m <= r:
                    cur = a[m]
                    counts[cur] -= 1
                    m += 1
                    if self.get_len(counts) == k:
                        break
                l = m
                print('>', l, r)
            
            if self.get_len(counts) == k:
                while m <= r:
                    cur = a[m]
                    if counts[cur] == 1:
                        break
                    else:
                        counts[cur] -= 1
                    m += 1
                print('<', l, m)
                count += m - l + 1
            r += 1
        return count

#print('result: {0}'.format(solution().subarray_with_k_distinct([27,27,43,28,11,20,1,4,49,18,37,31,31,7,3,31,50,6,50,46,4,13,31,49,15,52,25,31,35,4,11,50,40,1,49,14,46,16,11,16,39,26,13,4,37,39,46,27,49,39,49,50,37,9,30,45,51,47,18,49,24,24,46,47,18,46,52,47,50,4,39,22,50,40,3,52,24,50,38,30,14,12,1,5,52,44,3,49,45,37,40,35,50,50,23,32,1,2], 20)))
                
print('result: {0}'.format(solution().subarray_with_k_distinct([2,1,1,1,2], 2)))

