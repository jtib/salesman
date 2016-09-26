
from node import Node
from edge import EdgeException
from edge import Edge


import unittest

class TestEdge(unittest.TestCase):
    """
    Classe de tests unitaires de la classe Edge
    """

    def setUp(self):
        node1 = Node()
        node2 = Node()
        self.__edge = Edge(node1,node2)

    def test_count(self):
        "Verifie l'incrementation du compteur"
        prev_edge_count = self.__edge.get_count()
        node1 = Node()
        node2 = Node()
        edge2 = Edge(node1, node2)
        self.assertEqual(prev_edge_count + 1, self.__edge.get_count())

    def test_init(self):
        node = Node()
        with self.assertRaises(EdgeException):
            edge = Edge(node,node,1)



if __name__ == "__main__":
    unittest.main()