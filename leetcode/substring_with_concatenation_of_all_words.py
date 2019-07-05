class solution:
    def find_substring(self, s, words):
        if len(words) == 0:
            return []
        l_s = len(s)
        l_word = len(words[0])
        w_stats, s_stats = {}, {}
        for word in words:
            w_stats[word] = w_stats.get(word, 0) + 1
        for i in range(len(s)):
            sub_s = s[i:i + l_word]
            if sub_s in w_stats:
                s_stats[i] = sub_s

        def helper(start):
            end, res = start, []
            while start < l_s:
                if start in s_stats:
                    end = start
                    t_stats = w_stats.copy()
                    while end < l_s:
                        if end not in s_stats:
                            start = end + l_word
                            break
                        else:
                            sub_s = s_stats[end]
                            if t_stats.get(sub_s, 0) > 0:
                                end += l_word
                                t_stats[sub_s] -= 1
                                if t_stats[sub_s] == 0:
                                    del t_stats[sub_s]
                                    if len(t_stats) == 0:
                                        res.append(start)
                            else:
                                start_s = s_stats[start]
                                t_stats[start_s] = t_stats.get(start_s, 0) + 1
                                start += l_word
                    if end >= l_s:
                        break
                else:
                    start += l_word
            return res

        res = []
        for i in range(l_word):
            res += helper(i)
        return res

#print('result: {0}'.format(solution().find_substring('barfoothefoobarman', ['foo', 'bar'])))
#print('result: {0}'.format(solution().find_substring('barfoothefboobfarman', ['f', 'b'])))
#print('result: {0}'.format(solution().find_substring('barfoothefboobfarman', ['f'])))
#print('result: {0}'.format(solution().find_substring('', ['f', 'b'])))
#print('result: {0}'.format(solution().find_substring('', [])))
print('result: {0}'.format(solution().find_substring('wordgoodgoodgoodbestword', ['word','good','best','word'])))
