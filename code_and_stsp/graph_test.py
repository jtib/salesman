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
        node1 = Node(1)
        node2 = Node(2)
        with self.assertRaises(KeyError):
            self.__graph.add_edge(Edge(1,node1, node2))


    def test_get_nodes(self):
        "Verifie qu'on obtient bien la liste vide avec get_nodes sur un graphe vide"
        self.assertEqual(self.__graph.get_nodes(),[])


    def test_get_edges(self):
        "Verifie qu'on obtient bien la liste vide avec get_edges sur un graphe vide"
        self.assertEqual(self.__graph.get_edges(), [])

    def test_nb_nodes(self):
        "Teste le nombre de noeuds"
        node = Node(1)
        self.__graph.add_node(node)
        self.assertEqual(self.__graph.get_nb_nodes(),1)

    def test_nb_edges(self):
        "Teste le nombre d'aretes"
        node1 = Node(1)
        node2 = Node(2)
        self.__graph.add_node(node1)
        self.__graph.add_node(node2)
        self.__graph.add_edge(Edge(0,node1, node2))
        self.assertEqual(self.__graph.get_nb_edges(),1)
        
    def test_weight(self):
        "Teste le calcul du poids du graphe"
        node1 = Node(1)
        node2 = Node(2)
        self.__graph.add_node(node1)
        self.__graph.add_node(node2)
        self.__graph.add_edge(Edge(0, node1, node2,1))
        self.assertEqual(self.__graph.tree_weight(),1)





if __name__ == "__main__":
    unittest.main()