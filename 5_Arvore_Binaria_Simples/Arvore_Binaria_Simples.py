class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def get(self):
        return self.value
        
class BinaryTree:
    def __init__(self, value):
        node = TreeNode(value)
        self.root = node
    
    def in_order_traversal(self, root):
        if root:
            self.in_order_traversal(root.left)
            print(root.get(), end=" ")
            self.in_order_traversal(root.right)
        
new_tree = BinaryTree(1)
node_a = new_tree.root.left = TreeNode(2)
node_b = new_tree.root.right = TreeNode(3)
node_a_b = node_a.left = TreeNode(4)
node_b_a = node_b.right = TreeNode(5)
    
new_tree.in_order_traversal(new_tree.root)
