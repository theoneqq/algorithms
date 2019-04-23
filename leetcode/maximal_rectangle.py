class solution:
    def maximal_histogram(self, heights) -> int:
        res = 0
        rects = []
        heights.append(0)
        for i in range(0, len(heights)):
            while len(rects) != 0 and heights[i] <= heights[rects[-1]]:
                top_idx = rects[-1]
                rects.pop()
                res = max(res, ((top_idx + 1 if len(rects) == 0 else top_idx - rects[-1]) + i - top_idx - 1) * heights[top_idx])
            rects.append(i)
        return res

    def maximal_rectangle(self, matrix) -> int:
        m = []
        for row in range(0, len(matrix)):
            m.append([])
            for col in range(0, len(matrix[row])):
                m[row].append(0)

        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[row])):
                if row < 1:
                    m[row][col] = 1 if matrix[row][col] == 1 else 0
                else:
                    m[row][col] = m[row - 1][col] + 1 if matrix[row][col] == 1 else 0
        print(m)

        res = 0
        for row in range(0, len(m)):
            res = max(res, self.maximal_histogram(m[row]))

        return res

#print('result: {0}'.format(solution().maximal_histogram([2,1,5,6,2,3])))
print('result: {0}'.format(solution().maximal_rectangle([[1,0,1,0,0],[1,0,1,1,1,],[1,1,1,1,1],[1,0,0,1,0]])))
print('result: {0}'.format(solution().maximal_rectangle([[1,0,1,0,0]])))
print('result: {0}'.format(solution().maximal_rectangle([[0,1],[1,0]])))
