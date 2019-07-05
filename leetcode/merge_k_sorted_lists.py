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
        if len(lists) == 0:
            return None
        top_heap = [ [lists[i].val, i] for i in range(len(lists)) ]
        heapq.heapify(top_heap)
        sorted_notes = []
        while len(top_heap) > 0:
            min_node = heapq.heappop(top_heap)
            idx = min_node[1]
            node = lists[idx]
            sorted_notes.append(node)

            next_node = node.next
            if next_node != None:
                lists[idx] = next_node
                heapq.heappush(top_heap, [next_node.val, idx])

        for i in range(len(sorted_notes)):
            node, next_node = sorted_notes[i], sorted_notes[i + 1] if i + 1 < len(sorted_notes) else None
            node.next = next_node
        return sorted_notes[0]


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
solution().merge([n1, n4, n7])



