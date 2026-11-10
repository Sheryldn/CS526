import random

# ADT for Node
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# ADT for Binary Search Tree
class BST:
    def __init__(self):
        self.root = None

    # Add a node with given value
    def addNode(self, value):
        self.root = self._add_recursive(self.root, value)

    def _add_recursive(self, current, value):
        if current is None:
            return Node(value)
        if value < current.val:
            current.left = self._add_recursive(current.left, value)
        elif value > current.val:
            current.right = self._add_recursive(current.right, value)
        # Duplicate values are ignored
        return current

    # Delete a node with given value
    def deleteNode(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, current, value):
        if current is None:
            return None

        if value < current.val:
            current.left = self._delete_recursive(current.left, value)
        elif value > current.val:
            current.right = self._delete_recursive(current.right, value)
        else:
            # Node to delete found
            # Case 1 & 2: Leaf node or single child
            if current.left is None:
                return current.right
            if current.right is None:
                return current.left

            # Case 3: Two children - replace with inorder successor (min in right subtree)
            smallest_val = self._find_min(current.right)
            current.val = smallest_val
            current.right = self._delete_recursive(current.right, smallest_val)

        return current

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node.val

    # Search for a node with given value
    def findNode(self, value):
        return self._find_recursive(self.root, value)

    def _find_recursive(self, current, value):
        if current is None:
            return False
        if value == current.val:
            return True
        if value < current.val:
            return self._find_recursive(current.left, value)
        return self._find_recursive(current.right, value)

    # Visually print the tree structure
    def printTree(self):
        if self.root is None:
            print("Tree is empty.")
            return
        self._print_tree_helper(self.root, "", True)

    def _print_tree_helper(self, node, prefix, is_tail):
        if node is not None:
            print(prefix + ("└── " if is_tail else "├── ") + str(node.val))
            children = []
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
            for i, child in enumerate(children):
                self._print_tree_helper(child, prefix + ("    " if is_tail else "│   "), i == len(children) - 1)

def main():
    # Randomly generate dataset size between 5 and 50
    size = random.randint(5, 50)
    input_set = set()
    while len(input_set) < size:
        input_set.add(random.randint(1, 1000))
    
    input_list = list(input_set)
    print(f"Input Set (Size {size}): {input_list}")

    bst = BST()
    for val in input_list:
        bst.addNode(val)

    print("\n--- Initial BST ---")
    bst.printTree()

    # Demonstrate addNode
    new_val = random.randint(1, 1000)
    print(f"\nAdding new value: {new_val}")
    bst.addNode(new_val)
    print(f"--- Tree after addNode({new_val}) ---")
    bst.printTree()

    # Demonstrate deleteNode
    val_to_delete = input_list[0]
    print(f"\nDeleting value: {val_to_delete}")
    bst.deleteNode(val_to_delete)
    print(f"--- Tree after deleteNode({val_to_delete}) ---")
    bst.printTree()

    # Demonstrate findNode (Positive Case)
    pos_target = input_list[1]
    print(f"\nFind Node (Positive Case) for {pos_target}: {bst.findNode(pos_target)}")

    # Demonstrate findNode (Negative Case)
    neg_target = 9999
    print(f"Find Node (Negative Case) for {neg_target}: {bst.findNode(neg_target)}")

if __name__ == "__main__":
    main()