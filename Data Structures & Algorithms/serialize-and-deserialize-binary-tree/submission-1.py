class Codec:

    def serialize(self, root):
        a = []

        def dfs(n):
            if not n:
                a.append("#")
                return

            a.append(str(n.val))
            dfs(n.left)
            dfs(n.right)

        dfs(root)
        return ",".join(a)

    def deserialize(self, data):
        a = data.split(",")
        i = 0

        def dfs():
            nonlocal i

            if a[i] == "#":
                i += 1
                return None

            n = TreeNode(int(a[i]))
            i += 1

            n.left = dfs()
            n.right = dfs()

            return n

        return dfs()