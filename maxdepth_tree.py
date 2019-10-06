# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None:
            if root.right == None:
                return 1
            left=None
        left=root.left
        if root.right == None:
            right=None
        right=root.right
        depth = []
        depth.append(1)
        depth_l=1
        depth_r=1

        while left != None:
            depth_l += 1
            if left.right != None:
                depth.append(left.right.val)
            left = left.left

        left=root.left
        while right != None:
            depth_r += 1
            right = right.right

        print(depth_l, depth_r)
        if depth_l >= depth_r:
            depth = depth_l
        else:
            depth = depth_r
        return depth
        
