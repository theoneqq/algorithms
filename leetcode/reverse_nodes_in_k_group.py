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
    def reverse_nodes(self, head, k):
        if head == None or k <= 1:
            return head

        res, first, prev, cur, nxt, full = None, None, None, head, None, True
        def reverse(num):
            nonlocal res, first, cur, nxt, full
            if cur == None:
                return
            nxt = cur.next
            cur.next = None
            while num > 1 and nxt != None:
                if num == k:
                    first = cur
                tmp = nxt.next
                nxt.next = cur
                cur, nxt = nxt, tmp
                num -= 1
            full = num == 1
            if res == None and cur != None:
                res = cur

        while cur != None and full:
            reverse(k)
            if not full:
                reverse(k)
            if prev != None:
                prev.next = cur
            cur, prev = nxt, first

        return res


n1, n2, n3, n4, n5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
#print('result: {0}'.format(solution().reverse_nodes(n1, 0)))
#print('result: {0}'.format(solution().reverse_nodes(n1, 5)))
#print('result: {0}'.format(solution().reverse_nodes(n1, 4)))
print('result: {0}'.format(solution().reverse_nodes(n1, 3)))
print('result: {0}'.format(solution().reverse_nodes(n1, 2)))
#print('result: {0}'.format(solution().reverse_nodes(n1, 1)))
