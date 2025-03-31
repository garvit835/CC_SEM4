from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def left_view(root):
    if not root:
        return []

    result = []
    queue = deque([(root, 0)])  # (Node, Level)
    visited_levels = set()

    while queue:
        node, level = queue.popleft()

        if level not in visited_levels:
            result.append(node.value)
            visited_levels.add(level)

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    return result

# Example Usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)

print("Left View of Tree:", left_view(root))  # Output: [1, 2, 4, 8]
