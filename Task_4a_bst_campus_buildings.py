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
        """Inserts a new building into the BST while maintaining alphabetical key order."""
        self.root = self._insert_recursive(self.root, code.upper(), name)

    def _insert_recursive(self, current: BSTNode, code: str, name: str) -> BSTNode:
        if current is None:
            return BSTNode(code, name)
        if code < current.code:
            current.left = self._insert_recursive(current.left, code, name)
        elif code > current.code:
            current.right = self._insert_recursive(current.right, code, name)
        else:
            current.name = name  # Updates name if building code already exists
        return current


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

    print("Root node:", campus_bst.root.code, "-", campus_bst.root.name)
    print("Successfully inserted 10 buildings into the Campus BST.")
