class tree_node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class solution:
    def helper(self, root):
        if root.left != None:
            self.helper(root.left)
        self.v_nodes.append(root)
        if root.right != None:
            self.helper(root.right)

    def recover_tree(self, root):
        self.v_nodes = []
        self.helper(root)

        node_vals = [node.val for node in self.v_nodes]
        l = len(node_vals)

        m_count = 0
        while m_count < 2:
            for i in range(0, l - 1):
                if node_vals[i] > node_vals[i + 1]:
                    m_count += 1
                    j = i
                    while j + 1 < l and node_vals[j] > node_vals[j + 1]:
                        node_vals[j], node_vals[j + 1] = node_vals[j + 1], node_vals[j]
                        j += 1

        for node in self.v_nodes:
            print(node.val)
        for val in node_vals:
            print(val)
        
        m_idxs = []
        for i in range(0, l):
            if self.v_nodes[i].val != node_vals[i]:
                m_idxs.append(i)

        node1, node2 = self.v_nodes[m_idxs[0]], self.v_nodes[m_idxs[1]]
        node1.val, node2.val = node2.val, node1.val


n1 = tree_node(3)
n2 = tree_node(1)
n3 = tree_node(4)
n4 = tree_node(2)

n1.left = n2
n1.right = n3
n3.left = n4
'''
n1 = tree_node(1)
n2 = tree_node(3)
n3 = tree_node(2)
n1.left = n2
n2.right = n3
'''
solution().recover_tree(n1)

