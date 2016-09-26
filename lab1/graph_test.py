from node import Node
from graph import Graph
from edge import Edge


import unittest


class TestGraph(unittest.TestCase):
    """
    Classe de tests unitaires de la classe Graph. On ne teste pas
    le nombre de noeuds ni d'aretes pour des questions de variables
    locales et variables de classe.
    """

    def setUp(self):
        self.__graph= Graph('Graphe')

    def test_add_edge(self):
        "Verifie qu'on ne peut pas ajouter une arete sans ajouter les noeuds"
        node1 = Node()
        node2 = Node()
        with self.assertRaises(KeyError):
            self.__graph.add_edge(Edge(node1, node2))


    def test_get_nodes(self):
        "Verifie qu'on obtient bien la liste vide avec get_nodes sur un graphe vide"
        self.assertEqual(self.__graph.get_nodes(),[])


    def test_get_edges(self):
        "Verifie qu'on obtient bien la liste vide avec get_edges sur un graphe vide"
        self.assertEqual(self.__graph.get_edges(), [])




if __name__ == "__main__":
    unittest.main()