# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.val_set = set()

        self.val_set.add(root.val)
        self.iterate_node(root.left)
        self.iterate_node(root.right)

        print(self.val_set)
        if len(self.val_set) > 1:
            self.val_list_sorted = sorted(list(self.val_set))
            return self.val_list_sorted[1]

        return -1

    def iterate_node(self, node):
        if node is None:
            return

        self.val_set.add(node.val)
        self.iterate_node(node.left)
        self.iterate_node(node.right)
        