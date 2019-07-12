class solution:
    def trap(self, heights):
        len_heights = len(heights)
        l_max_height, r_max_height = 0, 0
        l, r = 0, len_heights - 1

        area = 0
        while l < r:
            if heights[l] < heights[r]:
                if l_max_height < heights[l]:
                    l_max_height = heights[l]
                else:
                    area += l_max_height - heights[l]
                l += 1
            else:
                if r_max_height < heights[r]:
                    r_max_height = heights[r]
                else:
                    area += r_max_height - heights[r]
                r += 1
        return area

                    
print('result: {0}'.format(solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])))
print('result: {0}'.format(solution().trap([0])))
print('result: {0}'.format(solution().trap([0,1])))
print('result: {0}'.format(solution().trap([])))
print('result: {0}'.format(solution().trap([1,0,1])))
print('result: {0}'.format(solution().trap([2,0,1])))
print('result: {0}'.format(solution().trap([5,2,1,2,1,5])))
print('result: {0}'.format(solution().trap([5,5,1,7,1,1,5,2,7,6])))
