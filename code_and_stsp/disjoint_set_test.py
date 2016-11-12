from node import Node
from disjoint_set import DisjointSet

import unittest

class TestDisjointSet(unittest.TestCase):
    """
    Classe de tests unitaires de la classe DisjointSet
    """

    def setUp(self):
        node0 = Node(iden = 0)
        node1 = Node(iden = 1)
        self.__disjoint_set = DisjointSet(node0)
        self.__other_disjoint_set = DisjointSet(node1)


    def test_set_node(self):
        "Verifie qu'on ne peut pas modifier l'attribut noeud"
        n = Node(iden = 1)
        with self.assertRaises(AttributeError):
            self.__disjoint_set.node = n


    def test_union_true(self):
        "Verifie qu'on peut joindre deux sets non connexes."
        self.assertEqual(self.__disjoint_set.union_sets(self.__other_disjoint_set), True)

    def test_union_false(self):
        "Verifie qu'on ne peut pas joindre deux sets connexes."
        self.__disjoint_set.union_sets(self.__other_disjoint_set)
        self.assertEqual(self.__disjoint_set.union_sets(self.__other_disjoint_set), False)

    def test_find_root(self):
        "Verifie qu'on obtient la racine s'il s'agit de l'element courant"
        self.assertEqual(self.__disjoint_set.find_root(), self.__disjoint_set)

    def test_find_root_rec(self):
        "Verifie qu'on obtient la racine s'il ne s'agit pas de l'element courant"
        self.__disjoint_set.union_sets(self.__other_disjoint_set)
        self.assertEqual(self.__other_disjoint_set.find_root(), self.__disjoint_set)


if __name__ == "__main__":
    unittest.main()

