class solution:
    def match(self, a: {}, k: int) -> bool:
        count = 0
        for num in a:
            if a[num] > 0:
                count += 1
        return count == k


    def subarray_with_k_distinct(self, a: [int], k: int) -> int:
        count = 0
        counts = {}
        list_len = len(a)

        l = 0
        r = 0
        print(a)
        while l <= r and r < list_len:
            while r < list_len and len(counts) < k:
                cur = a[r]
                print('right', cur, counts, len(counts))
                if cur not in counts:
                    counts[cur] = 1
                else:
                    counts[cur] += 1
                if len(counts) == k:
                    count += 1
                r += 1

            while l <= r and l < list_len and len(counts) >= k:
                cur = a[l]
                counts[cur] -= 1
                print('left', cur, counts, len(counts))
                if self.match(counts, k):
                #if len(counts) == k:
                    count += 1
                l += 1

        return count

print('result: {0}'.format(solution().subarray_with_k_distinct((1,2,1,2,3), 2)))
                

