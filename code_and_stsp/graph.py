import logging
import numpy as np
from node import Node
from disjoint_set import DisjointSet
from sys import maxsize
from heapq import heappush, heappop

class Graph(object):
    """
    Une classe generique pour representer un graphe comme un ensemble de
    noeuds.
    """
    def __init__(self, name='Sans nom'):
        self.__name = name
        self.__adj = {} # Matrice d'adjacence
        self.__edges = 0

    def add_node(self, node):
        "Ajoute un noeud au graphe."
        self.__adj.setdefault(node,{})

    def retrieve_nodes_from_id(self, *ids):
        "Renvoie les noeuds a partir de leurs ids."
        return [node for node in self.__adj.keys()
                if node.get_id() in ids]

    def add_edge(self, edge):
        "Ajoute une arete au graphe."
        (n1, n2) = edge.get_nodes()
        try:
            # checking if both nodes are there
            nodes = [self.__adj[n1], self.__adj[n2]]
            # checking if edge not already there
            if n2 not in self.__adj[n1]:
                # adding the new edge
                self.__adj[n1][n2] = self.__adj[n2][n1] = edge
                self.__edges += 1
        # if one (or both) node(s) missing
        except KeyError as ke:
            raise KeyError("At least node {0} missing. Add all nodes before\
                     adding edges.".format(ke))

    def get_name(self):
        "Donne le nom du graphe."
        return self.__name

    def get_nodes(self):
        "Donne la liste des noeuds du graphe."
        return self.__adj.keys()

    def get_nb_nodes(self):
        "Donne le nombre de noeuds du graphe."
        return len(self.get_nodes())

    def get_edges(self):
        "Donne la liste des aretes du graphe."
        edges = []
        edges.extend([v for n in self.get_nodes() for v in self.__adj[n].values()])
        return list(set(edges)) # removing doubles

    def get_nb_edges(self):
        "Donne le nombre d'aretes du graphe."
        return self.__edges

    def tree_weight(self):
        "Calcule le poids de l'arbre."
        return sum([e.get_weight() for e in self.get_edges()])

    def kruskal(self):
        "Retourne un arbre de recouvrement minimal s'il existe"
        min_tree = Graph('Arbre Minimal')

        disj_sets = {}

        nodes = self.get_nodes()
        # Le nombre de noeuds du graphe
        nb_nodes = self.get_nb_nodes
        # On remplit le dictionnaire de disjoint_sets
        for node in nodes:
            disj_sets[node] = DisjointSet(node)

        edges = self.get_edges()
        # La liste est triee selon la comparaison implementee dans edge
        edges.sort()

        # Construction de l'arbre
        for edge in edges:
            (node1,node2) = edge.get_nodes()

            # Si l'union des deux disjoint_sets est reussie
            if disj_sets[node1].union_sets(disj_sets[node2]):
                # On complete l'arbre minimal
                min_tree.add_node(node1)
                min_tree.add_node(node2)
                min_tree.add_edge(edge)
            # Si tous les noeuds sont dans min_tree, c'est que l'arbre est fini
            if min_tree.get_nb_nodes() == nb_nodes:
                break

        return min_tree

    def kruskal_pp(self):
        """Retourne un arbre de recouvrement minimal s'il existe,
        avec utilisation du rang et de la compression de chemins"""

        min_tree = Graph('Arbre Minimal')

        disj_sets = {}

        nodes = self.get_nodes()
        # Le nombre de noeuds du graphe
        nb_nodes = self.get_nb_nodes
        # On remplit le dictionnaire de disjoint_sets
        for node in nodes:
            disj_sets[node] = DisjointSet(node)

        edges = self.get_edges()
        # La liste est triee selon la comparaison implementee dans edge
        edges.sort()

        # Construction de l'arbre
        for edge in edges:
            (node1, node2) = edge.get_nodes()

            # Si l'union des deux disjoint_sets est reussie
            if disj_sets[node1].rank_compressed_union(disj_sets[node2]):
                # On complete l'arbre minimal
                min_tree.add_node(node1)
                logging.debug('Ajout de %s', node1)
                min_tree.add_node(node2)
                logging.debug('Ajout de %s', node2)
                min_tree.add_edge(edge)
                logging.debug('Ajout de %s', edge)
            # Si tous les noeuds sont dans min_tree, c'est que l'arbre est fini
            if min_tree.get_nb_nodes() == nb_nodes:
                break

        return min_tree

    def prim(self):
        "Algorithme de Prim"
        min_tree = Graph('Arbre Minimal')

        disj_sets = {}

        nodes = self.get_nodes()
        nb_nodes = self.get_nb_nodes

        # Choix de la racine (n'importe quel noeud)
        r = nodes[0]
        r.key = 0
        # File de priorite
        Q = []
        for node in nodes:
            disj_sets[node] = DisjointSet(node)
            heappush(Q, node)

        while len(Q) > 0:
            u = heappop(Q)
            logging.debug("Noeud ajoute a l'arbre minimal : %s", u)
            min_tree.add_node(u)
            if u.key is not 0:
                p = disj_sets[u].parent.node
                min_tree.add_edge(self.__adj[p][u])
            for v in [w for w in self.__adj[u].keys() if w in Q\
                    and self.__adj[u][w].get_weight() < w.key]:
                disj_sets[v].parent = disj_sets[u]
                v.key = self.__adj[u][v].get_weight()

        return min_tree


    def plot_graph(self):
        "Representation graphique du graphe avec Matplotlib."

        import matplotlib.pyplot as plt
        from matplotlib.collections import LineCollection

        fig = plt.figure()
        ax = fig.add_subplot(111)

        # Plot nodes
        nodes = self.get_nodes()
        try:
            x = [node.get_data()[0] for node in nodes]
            y = [node.get_data()[1] for node in nodes]

            # Plot edges
            edges = self.get_edges()
            edge_pos = np.asarray([(e.get_nodes()[0].get_data(),
                e.get_nodes()[1].get_data()) for e in edges])
            edge_collection = LineCollection(edge_pos, linewidth=1.5,
                    antialiased=True, colors=(.8, .8, .8), alpha=.75, zorder=0)
            ax.add_collection(edge_collection)
            ax.scatter(x, y, s=35, c='r', antialiased=True, alpha=.75, zorder=1)
            ax.set_xlim(min(x) - 10, max(x) + 10)
            ax.set_ylim(min(y) - 10, max(y) + 10)

            plt.ion()
            plt.show()
            plt.pause(0.001)
        except TypeError:
            print "Cannot display graph without node coordinates."
        return

    def __repr__(self):
        name = self.get_name()
        nb_nodes = self.get_nb_nodes()
        nb_edges = self.get_nb_edges()
        s = 'Graphe %s comprenant %d noeuds et %d aretes' % (name, nb_nodes, nb_edges)
        for node in self.get_nodes():
            s += '\n  ' + repr(node)
        for edge in self.get_edges():
            s += '\n  ' + repr(edge)
        s += '\n' + 'Poids total : ' + repr(self.tree_weight())
        return s


if __name__ == '__main__':
    from node import Node
    from edge import Edge
    G = Graph(name='Graphe test')
    count = 0
    for k in range(5):
        n1 = Node(iden=count, name='test %d' % count)
        G.add_node(n1)
        count += 1
        n2 = Node(iden=count, name='test %d' % count)
        G.add_node(n2)
        count += 1
        G.add_edge(Edge(k, n1, n2, weight=42))
    print G
