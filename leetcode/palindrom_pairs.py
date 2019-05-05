class solution:
    def check_imp(self, idx, p_word, direction):
        if p_word in self.w_hash:
            p_idx = self.w_hash[p_word]
            if p_idx != idx:
                if p_word == '':
                    self.r_hash[(p_idx, idx)] = 1
                    self.r_hash[(idx, p_idx)] = 1
                else:
                    if direction == 0:
                        self.r_hash[(p_idx, idx)] = 1
                    else:
                        self.r_hash[(idx, p_idx)] = 1

    def check_left(self, idx):
        word = self.words[idx]
        wl = len(word)
        start, end, step = 0, wl, 1
        while start < end:
            l1, l2, r = word[start+1:], word[start:], word[:start+1][::-1]
            if r.find(l1) == 0:
                self.check_imp(idx, r[len(l1):], 1)
            if r.find(l2) == 0:
                self.check_imp(idx, r[len(l2):], 1)
            start += 1

    def check_right(self, idx):
        word = self.words[idx]
        wl = len(word)
        start, end, step = wl - 1, 0, -1
        while start > end:
            l1, l2, r = word[:start], word[:start+1], word[start:]
            rl1, rl2 = l1[::-1], l2[::-1]
            if r.find(rl1) == 0:
                self.check_imp(idx, r[len(rl1):][::-1], 0)
            if r.find(rl2) == 0:
                self.check_imp(idx, r[len(rl2):][::-1], 0)
            start -= 1


    def check(self, idx):
        word = self.words[idx]
        wl = len(word)
        if wl == 0:
            return
        self.check_left(idx)
        self.check_right(idx)


    def palindrom_pairs(self, words):
        self.words = words
        self.r_hash = {}
        self.w_hash = {}
        for i in range(0, len(self.words)):
            self.w_hash[self.words[i]] = i
        for i in range(0, len(self.words)):
            self.check(i)

        return [ [k[0], k[1]] for k in self.r_hash ]

res = solution().palindrom_pairs(['abcd', 'dcba', 'lls', 's', 'sssll'])
for pair in res:
    print(pair[0], pair[1])
