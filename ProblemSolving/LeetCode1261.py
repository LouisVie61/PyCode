from ProblemSolving.LeetCode100 import TreeNode


class FindElements:

    def __init__(self, root: TreeNode):
        if not root:
            return

        self.recovered_value = set()
        self.recovered_value.add(0)
        root.val = 0

        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                node.left.val = 2 * node.val + 1
                self.recovered_value.add(node.left.val)
                stack.append(node.left)

            if node.right:
                node.right.val = 2 * node.val + 2
                self.recovered_value.add(node.right.val)
                stack.append(node.right)


    def find(self, target: int) -> bool:
        return target in self.recovered_value