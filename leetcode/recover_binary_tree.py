class tree_node:
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None

class solution:
    def helper(self, root):
        if root.left != None:
            root.left.left_parent = root
            self.helper(root.left)
        self.v_nodes.append(root)
        if root.right != None:
            root.right.right_parent = root
            self.helper(root.right)

    def swap(self, node1, node2):
        node1.left, node2.left = node2.left, node1.left
        node1.right, node2.right = node2.right, node1.right

        if hasattr(node1, 'left_parent'):
            node1.left_parent.left = node2
        elif hasattr(node1, 'right_parent'):
            node1.right_parent.right = node2
        if hasattr(node2, 'left_parent'):
            node2.left_parent.left = node1
        elif hasattr(node2, 'right_parent'):
            node2.right_parent.right = node1

    def recover_tree(self, root):
        self.v_nodes = []
        self.helper(root)

        r_nodes = self.v_nodes.copy()
        l = len(r_nodes)
        for i in range(0, l):
            j = i + 1
            while j < l and r_nodes[i].val > r_nodes[j].val:
                r_nodes[i], r_nodes[j] = r_nodes[j], r_nodes[i]
                j += 1
        
        m_idxs = []
        for i in range(0, l):
            if self.v_nodes[i].val != r_nodes[i].val:
                m_idxs.append(i)

        node1, node2 = self.v_nodes[m_idxs[0]], self.v_nodes[m_idxs[1]]
        self.swap(node1, node2)


n1 = tree_node(1)
n2 = tree_node(2)
n3 = tree_node(3)

n1.left = n1
n2.right = n3
solution().recover_tree(n1)
