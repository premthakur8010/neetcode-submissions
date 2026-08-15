class Solution:
    def buildTree(self, preorder, inorder):
        pos = {v: i for i, v in enumerate(inorder)}
        i = 0

        def build(l, r):
            nonlocal i

            if l > r:
                return None

            v = preorder[i]
            i += 1

            root = TreeNode(v)
            p = pos[v]

            root.left = build(l, p - 1)
            root.right = build(p + 1, r)

            return root

        return build(0, len(inorder) - 1)