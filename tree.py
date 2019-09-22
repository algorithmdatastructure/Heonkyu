"""
1. Merging Tree
https://leetcode.com/problems/merge-two-binary-trees/
"""
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left,t2.left)
        t1.right = self.mergeTrees(t1.right,t2.right)
        return t1

"""
2. Postorder Traversal
https://leetcode.com/problems/n-ary-tree-postorder-traversal/
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root == None:
            return []
        if root.children == None:
            return [root.val]
        l = []
        for i in root.children:
            r=self.postorder(i)
            l=l+r
        l=l+[root.val]
        return l
    
"""
3. Invert binary Tree
https://leetcode.com/problems/invert-binary-tree/
"""
class Solution(object):
    def invertTree(self, root):
        if root:
            root.right, root.left = root.left, root.right
            self.invertTree(root.right)
            self.invertTree(root.left)
        return root
