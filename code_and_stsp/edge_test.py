
from node import Node
from edge import EdgeException
from edge import Edge


import unittest

class TestEdge(unittest.TestCase):
    """
    Classe de tests unitaires de la classe Edge
    """

    def setUp(self):
        node1 = Node(1)
        node2 = Node(2)
        self.__edge = Edge(1,node1,node2)

    def test_init(self):
        node = Node(1)
        with self.assertRaises(EdgeException):
            edge = Edge(2,node,node,1)


if __name__ == "__main__":
    unittest.main()