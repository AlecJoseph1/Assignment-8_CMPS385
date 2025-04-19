class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

def find_node(root, key):
    if not root:
        return None
    if root.key == key:
        return root
    elif key < root.key:
        return find_node(root.left, key)
    else:
        return find_node(root.right, key)

def leftrotation(node_key, root):
    node = find_node(root, node_key)
    if not node or not node.right:
        return root

    new_root = node.right
    node.right = new_root.left
    if new_root.left:
        new_root.left.parent = node

    new_root.left = node
    new_root.parent = node.parent
    node.parent = new_root

    if new_root.parent:
        if new_root.parent.left == node:
            new_root.parent.left = new_root
        else:
            new_root.parent.right = new_root
    else:
        root = new_root

    return root

def rightrotation(node_key, root):
    node = find_node(root, node_key)
    if not node or not node.left:
        return root

    new_root = node.left
    node.left = new_root.right
    if new_root.right:
        new_root.right.parent = node

    new_root.right = node
    new_root.parent = node.parent
    node.parent = new_root

    if new_root.parent:
        if new_root.parent.left == node:
            new_root.parent.left = new_root
        else:
            new_root.parent.right = new_root
    else:
        root = new_root

    return root

# Utility function to print the tree structure
def print_tree(node, prefix="", is_left=True):
    if node:
        print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.key))
        print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

# Building a sample tree
"""
       30
      /  \
    20    40
             \
             50
"""

root = TreeNode(30)
node20 = TreeNode(20)
node40 = TreeNode(40)
node50 = TreeNode(50)

root.left = node20
root.right = node40
node20.parent = root
node40.parent = root
node40.right = node50
node50.parent = node40

print("Original Tree:")
print_tree(root)

# Perform left rotation at node 30
root = leftrotation(30, root)

print("\nAfter Left Rotation at 30:")
print_tree(root)

# Perform right rotation at new root (40)
root = rightrotation(40, root)

print("\nAfter Right Rotation at 40:")
print_tree(root)