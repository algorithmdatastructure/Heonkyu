# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        l = []
        l.append(root.val)
        left=root.left
        right=root.right

        while left != None:
            l.append(left.val)
            if left.right != None:
                l.append(left.right.val)
            left = left.left

        left=root.left
        while right != None:
            l.append(right.val)
            if right.left != None:
                l.append(right.left.val)
            right = right.right

        l.sort()
        print(l)

        global tree
        tree = TreeNode(l[0])
        for i in range(1, len(l)):
            right = tree.right
            right = TreeNode(l[i])

        print(tree)
        return tree
