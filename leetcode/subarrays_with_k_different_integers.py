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
        r = 0
        while l <= r and r < list_len:
            cur = a[r]
            if cur not in counts:
                counts[cur] = 1
            else:
                counts[cur] += 1
            counts_len = self.get_len(counts)
            print('counts', counts)
            if counts_len > k:
                while l <= r:
                    cur = a[l]
                    counts[cur] -= 1
                    if self.get_len(counts) < k:
                        if cur not in counts:
                            counts[cur] = 1
                        else:
                            counts[cur] += 1
                        break
                    l += 1
                count += 1
                print('>', l, r)
            elif counts_len == k:
                m = l
                while m <= r:
                    cur = a[m]
                    if counts[cur] == 1:
                        break
                    else:
                        counts[cur] -= 1
                    m += 1
                print('<', l, m)
                for i in range(l, m):
                    cur = a[i]
                    if cur not in counts:
                        counts[cur] = 1
                    else:
                        counts[cur] += 1
                count += m - l + 1
            r += 1
        return count

print('result: {0}'.format(solution().subarray_with_k_distinct((1,2,1,2,1,2), 2)))
                

