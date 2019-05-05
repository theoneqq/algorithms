class solution:
    def check_from_left(self, idx):
        word = self.words[idx]
        for i in range(0, len(word)):
            l, r = word[:i], word[i:]
            #print('left', l, r)
            if r.find(l[::-1]) == 0:
                cr = r[len(l):][::-1]
                if cr in self.w_hash:
                    p_idx = self.w_hash[cr]
                    if p_idx != idx:
                        self.r_hash[self.w_hash[cr]] = idx

    def check_from_right(self, idx):
        word = self.words[idx]
        for i in range(len(word) - 1, -1, -1):
            l, r = word[:i], word[i:]
            #print('right', l, r)
            if l.rfind(r[::-1]) == 0:
                cl = l[:-len(r)][::-1]
                if cl in self.w_hash:
                    p_idx = self.w_hash[cl]
                    if p_idx != idx:
                        self.r_hash[self.w_hash[cl]] = idx

    def check(self, idx):
        self.check_from_left(idx)
        self.check_from_right(idx)

    def palindrom_pairs(self, words):
        self.words = words
        self.r_hash = {}
        self.w_hash = {}
        for i in range(0, len(self.words)):
            self.w_hash[self.words[i]] = i
        for i in range(0, len(self.words)):
            self.check(i)

        return [ [k, self.r_hash[k]] for k in self.r_hash ]

res = solution().palindrom_pairs(['bat', 'tab', '', ''])
for pair in res:
    print(pair[0], pair[1])
