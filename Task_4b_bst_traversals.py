class BSTNode:
    """Represents a single campus building in the Binary Search Tree."""
    def __init__(self, code: str, name: str):
        self.code = code
        self.name = name
        self.left = None
        self.right = None


class CampusBST:
    """Binary Search Tree storing campus buildings keyed by building code."""
    def __init__(self):
        self.root = None

    def insert(self, code: str, name: str) -> None:
        self.root = self._insert_recursive(self.root, code.upper(), name)

    def _insert_recursive(self, current: BSTNode, code: str, name: str) -> BSTNode:
        if current is None:
            return BSTNode(code, name)
        if code < current.code:
            current.left = self._insert_recursive(current.left, code, name)
        elif code > current.code:
            current.right = self._insert_recursive(current.right, code, name)
        return current

   # Traversals
    def inorder(self) -> list[str]:
        """Left subtree -> Root -> Right subtree"""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: BSTNode, result: list[str]) -> None:
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.code)
            self._inorder_recursive(node.right, result)

    def preorder(self) -> list[str]:
        """Root -> Left subtree -> Right subtree"""
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node: BSTNode, result: list[str]) -> None:
        if node is not None:
            result.append(node.code)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder(self) -> list[str]:
        """Left subtree -> Right subtree -> Root"""
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node: BSTNode, result: list[str]) -> None:
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.code)


if __name__ == "__main__":
    campus_bst = CampusBST()
    buildings = [
        ("LIB", "Library"),
        ("HST", "Hostel"),
        ("LEC1", "Lecture hall 1"),
        ("LEC2", "Lecture hall 2"),
        ("ADM", "Administration"),
        ("ICT", "ICT lab"),
        ("MED", "Sickbay"),
        ("SPT", "Sports office"),
        ("CAF", "Cafeteria"),
        ("RAD", "Campus radio")
    ]

    for code, name in buildings:
        campus_bst.insert(code, name)

    print("Inorder Traversal:  ", " -> ".join(campus_bst.inorder()))
    print("Preorder Traversal: ", " -> ".join(campus_bst.preorder()))
    print("Postorder Traversal:", " -> ".join(campus_bst.postorder()))
