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
        if head == None:
            return None
        res, prev, num = head, None, k
        cur_node, next_node = head, head.next

        while num > 1 and next_node != None:
            if num == k and prev != None:
                prev = cur_node
            tmp = next_node.next
            next_node.next = cur_node
            cur_node, next_node = next_node, tmp
            num -= 1
            if num == 1:
                if prev != None:
                    prev.next = cur_node
                else:
                    res = cur_node
                num = k
        print('yoho')

        if num != 1:
            next_node = cur_node.next
            while next_node != None:
                tmp = next_node.next
                next_node.next = cur_node
                cur_node, next_node = next_node, tmp
            prev.next = cur_node

        return res


n1, n2, n3 = ListNode(1), ListNode(4), ListNode(5)
n1.next = n2
n2.next = n3
print('result: {0}'.format(solution().reverse_nodes(n1, 2)))
