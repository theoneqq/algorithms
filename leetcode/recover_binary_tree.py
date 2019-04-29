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

        r_node_vals = [ node.val for node in self.v_nodes]
        l = len(r_node_vals)
        for i in range(0, l):
            j = 0
            while j + 1 < l and r_node_vals[j] > r_node_vals[j + 1]:
                r_node_vals[j], r_node_vals[j + 1] = r_node_vals[j + 1], r_node_vals[j]
                j += 1

        for node in self.v_nodes:
            print(node.val)
        for val in r_node_vals:
            print(val)
        
        m_idxs = []
        for i in range(0, l):
            if self.v_nodes[i].val != r_node_vals[i]:
                m_idxs.append(i)

        node1, node2 = self.v_nodes[m_idxs[0]], self.v_nodes[m_idxs[1]]
        node1.val, node2.val = node2.val, node1.val


n1 = tree_node(1)
n2 = tree_node(2)
n3 = tree_node(3)

n1.left = n3
n3.right = n2

solution().recover_tree(n1)

print(n1.val, n2.val, n3.val)
