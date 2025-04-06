class Node:
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
#node_gr += greatest_node(root.left_child)

def greatest_node(root: Node):
    node_gr = root.value
    if root.left_child is not None:
        if root.left_child.value > node_gr:
            node_gr = root.left_child.value
            greatest_node(root.left_child)
        else:
            df
    if root.right_child is not None:
        if root.right_child.value > node_gr:
            node_gr = root.right_child.value
            node_gr = greatest_node(root.right_child)
        else:
            fg
    return node_gr

if __name__ == "__main__":
    tree = Node(2)
    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)
    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)
    print(greatest_node(tree))