from collections import deque

from ProblemSolving.LeetCode100 import TreeNode

# build ordinary binary tree: hard problem in LeetCode

def extractNodes(traversal: str) -> list:
    nodes = []
    traversal = list(traversal)
    index_first = 0
    root = ""

    # Process the root with multiple digit:
    # note: be careful with the variable that increasing by itself
    while index_first < len(traversal) and traversal[index_first] != '-':
        root += traversal[index_first]
        index_first += 1

    nodes.append((0, int(root)))
    cnt_dash = 0
    i = index_first

    while i < len(traversal):
        if traversal[i] == '-':
            cnt_dash += 1
        else:
            # process the child node has multiple digit
            # was struggled with index out of bound
            num = ""
            while i < len(traversal) and traversal[i].isdigit():
                num += traversal[i]
                i += 1
            nodes.append((cnt_dash, int(num)))
            cnt_dash = 0
            continue # skip manual index increment below
        i += 1

    return nodes


def build_binary_tree(traversal: str) -> TreeNode:
    nodes = extractNodes(traversal)
    stack = []

    for depth, num in nodes:
        node = TreeNode(num)

        while len(stack) > depth:
            stack.pop()

        if stack:
            parent = stack[-1]
            if not parent.left:
                parent.left = node
            else:
                parent.right = node

        stack.append(node)

    return stack[0] if stack else None

def levelOrderTraversal(traversal: str) -> list:
    bt = build_binary_tree(traversal)

    if not bt:
        return []

    result = []
    queue = deque([bt])

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    return result

test1 = "10-7--8"
print(levelOrderTraversal(test1))

test2 = "1-2--3--4-5--6--7"
print(levelOrderTraversal(test2))
