class interval:
    def __init__(self, s = 0, e = 0):
        self.start = s
        self.end = e

class solution:
    def insert(self, intervals, new_interval) -> []:
        result_intervals = []
        start, end = -1, -1
        new_start, new_end = new_interval.start, new_interval.end
        for cur_interval in intervals:
            cur_start, cur_end = cur_interval.start, cur_interval.end
            if start == -1:
                if new_start <= cur_start:
                    start = new_start
                elif new_start <= cur_end:
                    start = cur_start
                else:
                    result_intervals.append(cur_interval)
                if start != -1 and end == -1:
                    if new_end <= cur_end:
                        end = cur_end
                        result_intervals.append(interval(start, end))
            elif end == -1:
                if new_end < cur_start:
                    end = new_end
                    result_intervals.append(interval(start, end))
                    result_intervals.append(cur_interval)
                elif new_end <= cur_end:
                    end = cur_end
                    result_intervals.append(interval(start, end))
            else:
                result_intervals.append(cur_interval)
        if end == -1:
            result_intervals.append(interval(start, new_end))

        return result_intervals


intervals = [interval(1, 2), interval(3, 5), interval(6, 7), interval(8, 10), interval(12, 16)]
new_interval = interval(12, 16)
intervals = solution().insert(intervals, new_interval)

for interval in intervals:
    print('{0}\t{1}'.format(interval.start, interval.end))
