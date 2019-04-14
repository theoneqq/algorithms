class solution:
    def __init__(self):
        self.count = 0

    def can(self, used, cur) -> bool:
        x1, y1 = len(used) + 1, cur
        for i in range(0, len(used)):
            x2, y2 = i + 1, used[i]
            diff_x, diff_y = x1 - x2, y1 - y2
            if diff_x == 0 or diff_y == 0 or abs(diff_x / diff_y) == 1:
                return False
        return True
    
    def helper(self, available, used):
        if len(available) == 0:
            self.count += 1
            return

        has_next = False
        for num in available:
            if self.can(used, num):
                has_next = True
                del available[num]
                used.append(num)
                self.helper(available, used)
                available[num] = 1
                used.pop()

        if not has_next:
            return


    def total_n_queens(self, n: int) -> int:
        available = {}
        for i in range(0, n):
            available[i + 1] = 1
        used = []
        self.helper(available, used)
        return self.count

print('result: {0}'.format(solution().total_n_queens(4)))
