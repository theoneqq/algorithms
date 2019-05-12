import heapq
class node():
    def __init__(self, num, idx):
        self.num = num
        self.idx = idx

    def __lt__(self, rhs):
        return self.num <= rhs.num

class solution():
    def smallest_range(self, nums) ->[]:
        out_min = -100000
        nl = len(nums)
        idxs = [ 0 for i in range(nl) ]
        left, right = min([ nums[i][-1] for i in range(nl) ]), max([ nums[i][-1] for i in range(nl) ])
        d = right - left
        
        top_heap = [ node(nums[i][0], i) for i in range(nl) ]
        heapq.heapify(top_heap)

        while idxs != [ len(l) - 1 for l in nums ]:
            max_node = heapq.nlargest(1, top_heap)[0]
            min_node = heapq.heappop(top_heap)

            cur_min, cur_max = min_node.num, max_node.num
            true_min = min(cur_min, out_min) if out_min != -100000 else cur_min

            if cur_max - true_min < d or (cur_max - true_min == d and true_min < left):
                left, right, d = true_min, cur_max, cur_max - true_min

            min_idx = min_node.idx
            if idxs[min_idx] + 1 >= len(nums[min_idx]):
                out_min = min(out_min, cur_min)
            else:
                idxs[min_idx] += 1
                heapq.heappush(top_heap, node(nums[min_idx][idxs[min_idx]], min_idx))

        return [left, right]


ls = [[1, 9, 15, 24, 36], [0, 9, 12, 40], [-5, 18, 22, 30]]
#ls = [[-5,-4,-3,-2,-1,1], [1,2,3,4,5]]
#ls = [[1,3,5,7,9,10], [2,4,6,8,10]]
print('result: {0}'.format(solution().smallest_range(ls)))
