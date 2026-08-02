# DSA Implementation Draft for DSA-102: Dynamic Programming 2D Memoization & Space Optimization
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val: int) -> None:
        """Insert value into BST in O(log N) time complexity."""
        if not self.root:
            self.root = TreeNode(val)
            return
        
        curr = self.root
        while curr:
            if val < curr.val:
                if not curr.left:
                    curr.left = TreeNode(val)
                    break
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = TreeNode(val)
                    break
                curr = curr.right
