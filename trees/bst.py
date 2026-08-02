## TEsting 101
## TEsting 102
## TEsting 103

# DSA Implementation for DSA-101: Implement Binary Search Tree & Graph BFS Algorithm
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

    def search(self, val: int) -> bool:
        """Search value in BST in O(log N) average time complexity."""
        curr = self.root
        while curr:
            if curr.val == val: return True
            curr = curr.left if val < curr.val else curr.right
        return False
