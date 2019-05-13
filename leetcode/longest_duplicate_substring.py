class solution:
    def cal_hash(self, chars):
        h = 0
        cl = len(chars)
        for i in range(cl):
            h += ((ord(chars[i]) - 97) * (26 ** (cl - i - 1))) % self.p
        return h % self.p

    def find_k(self, s, k):
        peieces = {}
        prev_peiece = s[:k]
        prev_peiece_hash = self.cal_hash(prev_peiece)
        peieces[prev_peiece_hash] = [prev_peiece]

        for i in range(1, self.l - k + 1):
            new_peiece = s[i:i + k]
            new_peiece_hash = ((prev_peiece_hash - (ord(prev_peiece[0]) - 97) * (26 ** (k - 1))) * 26 + (ord(new_peiece[-1]) - 97)) % self.p
            if new_peiece_hash in peieces:
                for peiece in peieces[new_peiece_hash]:
                    if peiece == new_peiece:
                        return new_peiece
                peieces[new_peiece_hash].append(new_peiece)
            else:
                peieces[new_peiece_hash] = [new_peiece]
            
            prev_peiece, prev_peiece_hash = new_peiece, new_peiece_hash
        return ''

    def longest_duplicate_substring(self, s):
        self.p = 16777619
        self.l = len(s)
        res, low, high = '', 1, self.l
        while low <= high:
            mid = (low + high) // 2
            cur_res = self.find_k(s, mid)
            if cur_res != '':
                res = cur_res
                low = mid + 1
            else:
                high = mid - 1
        return res


#print('cal hash: {0}'.format(solution().cal_hash(['b', 'a', 'n'])))
print('result: {0}'.format(solution().longest_duplicate_substring('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')))
