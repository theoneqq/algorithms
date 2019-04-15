class solution:
    def insert(self, intervals, new_interval):
        all_intervals = intervals + [new_interval]
        all_intervals = sorted(all_intervals, key = lambda x:x.start)
        out = []
        out.append(all_intervals[0])
        for i in range(1, len(all_intervals)):
            if out[-1].end >= all_intervals[i].start:
                out[-1].end = max(out[-1].end, all_intervals[i].end)
            else:
                out.append(all_intervals[i])
        return out
