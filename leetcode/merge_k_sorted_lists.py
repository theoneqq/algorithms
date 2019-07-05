import heapq
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        s = str(self.val)
        if self.next != None:
            s += '->' + str(self.next)
        return s

class solution:
    def merge(self, lists):
        top_heap = []
        for i in range(len(lists)):
            node = lists[i]
            if node != None:
                top_heap.append([node.val, i])
        heapq.heapify(top_heap)
        sorted_nodes = []
        while len(top_heap) > 0:
            min_node = heapq.heappop(top_heap)
            idx = min_node[1]
            node = lists[idx]
            sorted_nodes.append(node)

            next_node = node.next
            if next_node != None:
                lists[idx] = next_node
                heapq.heappush(top_heap, [next_node.val, idx])

        for i in range(len(sorted_nodes)):
            node, next_node = sorted_nodes[i], sorted_nodes[i + 1] if i + 1 < len(sorted_nodes) else None
            node.next = next_node
        return sorted_nodes[0] if len(sorted_nodes) > 0 else None


n1, n2, n3 = ListNode(1), ListNode(4), ListNode(5)
n1.next = n2
n2.next = n3

n4, n5, n6 = ListNode(1), ListNode(3), ListNode(4)
n4.next = n5
n5.next = n6

n7, n8 = ListNode(2), ListNode(6)
n7.next = n8

#print(n7)
#print('result: {0}'.format(solution().merge([n1, n4, n7])))
#print('result: {0}'.format(solution().merge([n1])))
#print('result: {0}'.format(solution().merge([n1, None, n4])))
print('result: {0}'.format(solution().merge([None, None, None])))
#solution().merge([n1, n4, n7])



