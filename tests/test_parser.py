import unittest
from parser import ASTNode

class TestASTNode(unittest.TestCase):
    """
    Test suite for the ASTNode class.

    This test class contains unit tests to verify the functionality of the ASTNode class,
    including its initialization, string representation, and handling of child nodes.

    Tests:
    - `test_astnode_initialization`: Verifies that an ASTNode instance is correctly initialized
        with the specified type, value, and an empty list of children.
    - `test_astnode_repr`: Checks the string representation of an ASTNode instance to ensure
        it matches the expected format.
    - `test_astnode_children`: Tests the ability to add child nodes to an ASTNode instance
        and verifies the correctness of the children list.
    """
    def test_astnode_initialization(self):
        node = ASTNode(type="NUMBER", value=42)
        self.assertEqual(node.type, "NUMBER")
        self.assertEqual(node.value, 42)
        self.assertEqual(node.children, [])

    def test_astnode_repr(self):
        node = ASTNode(type="NUMBER", value=42)
        self.assertEqual(repr(node), "ASTNode(NUMBER, 42, [])")

    def test_astnode_children(self):
        parent = ASTNode(type="PARENT")
        child1 = ASTNode(type="CHILD1", value="child1_value")
        child2 = ASTNode(type="CHILD2", value="child2_value")
        parent.children.append(child1)
        parent.children.append(child2)
        self.assertEqual(len(parent.children), 2)
        self.assertEqual(parent.children[0].type, "CHILD1")
        self.assertEqual(parent.children[1].type, "CHILD2")

if __name__ == '__main__':
    unittest.main()