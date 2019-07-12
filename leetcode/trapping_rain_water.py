class solution:
    def trap(self, heights):
        h_points = []
        len_heights = len(heights)

        for i in range(len_heights):
            m_point = heights[i]
            l_point = heights[i - 1] if i > 0 else -1
            r_point = heights[i + 1] if i + 1 < len_heights else -1
            if (m_point >= l_point and m_point >= r_point) and not (m_point == l_point and m_point == r_point):
                h_points.append((i, m_point))

        def cal(start, end):
            print(start, ':', end)
            res = 0
            std_height = min(heights[start], heights[end])
            for i in range(start, end + 1):
                res += max(0, std_height - heights[i])
            return res

        area, start = 0, 0
        len_points = len(h_points)
        while start < len_points - 1:
            i_height = h_points[start][1]
            end = start + 1
            for j in range(start + 1, len_points):
                j_height = h_points[j][1]
                if j_height >= i_height:
                    end = j
                    break
                else:
                    if j_height > h_points[end][1]:
                        end = j
            area += cal(h_points[start][0], h_points[end][0])
            start = end

        return area
                    
'''
print('result: {0}'.format(solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])))
print('result: {0}'.format(solution().trap([0])))
print('result: {0}'.format(solution().trap([0,1])))
print('result: {0}'.format(solution().trap([])))
print('result: {0}'.format(solution().trap([1,0,1])))
print('result: {0}'.format(solution().trap([2,0,1])))
print('result: {0}'.format(solution().trap([5,2,1,2,1,5])))
'''
print('result: {0}'.format(solution().trap([5,5,1,7,1,1,5,2,7,6])))
