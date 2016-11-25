import logging
import numpy as np
from node import Node
from edge import Edge
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
                if node.id in ids]

    def add_edge(self, edge):
        "Ajoute une arete au graphe."
        (n1, n2) = edge.nodes
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

    @property
    def name(self):
        "Donne le nom du graphe."
        return self.__name

    @property
    def nodes(self):
        "Donne la liste des noeuds du graphe."
        return self.__adj.keys()

    def get_nb_nodes(self):
        "Donne le nombre de noeuds du graphe."
        return len(self.nodes)

    @property
    def edges(self):
        "Donne la liste des aretes du graphe."
        edges = []
        edges.extend([v for n in self.nodes for v in self.__adj[n].values()])
        return list(set(edges)) # removing doubles

    @property
    def adj(self):
        "Retourne la liste d'adjacence"
        return self.__adj

    def get_nb_edges(self):
        "Donne le nombre d'aretes du graphe."
        return len(self.edges)

    def tree_weight(self):
        "Calcule le poids de l'arbre."
        return sum([e.weight for e in self.edges])

    def kruskal(self):
        "Retourne un arbre de recouvrement minimal s'il existe"
        min_tree = Graph('Arbre Minimal')

        disj_sets = {}

        nodes = self.nodes

        # Le nombre de noeuds du graphe
        nb_nodes = self.get_nb_nodes()

        # On remplit le dictionnaire de disjoint_sets
        for node in nodes:
            disj_sets[node] = DisjointSet(node)

        edges = self.edges

        # La liste est triee selon la comparaison implementee dans edge
        edges.sort()

        # Construction de l'arbre
        for edge in edges:
            (node1,node2) = edge.nodes

            # Si l'union des deux disjoint_sets est reussie
            if disj_sets[node1].union_sets(disj_sets[node2]):
                # On complete l'arbre minimal
                min_tree.add_node(node1)
                min_tree.add_node(node2)
                min_tree.add_edge(edge)

            # Si tous les noeuds sont dans min_tree, c'est que l'arbre est fini
            if min_tree.get_nb_edges() == nb_nodes-1:
                break

        return min_tree

    def kruskal_pp(self):
        """Retourne un arbre de recouvrement minimal s'il existe,
        avec utilisation du rang et de la compression de chemins"""

        min_tree = Graph('Arbre Minimal')

        disj_sets = {}

        nodes = self.nodes

        # Le nombre de noeuds du graphe
        nb_nodes = self.get_nb_nodes()

        # On remplit le dictionnaire de disjoint_sets
        for node in nodes:
            disj_sets[node] = DisjointSet(node)

        edges = self.edges

        # La liste est triee selon la comparaison implementee dans edge
        edges.sort()

        # Construction de l'arbre
        for edge in edges:
            (node1, node2) = edge.nodes

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
            if min_tree.get_nb_edges() == nb_nodes-1:
                break

        return min_tree

    def prim(self, root = "default"):
        "Algorithme de Prim"

        min_tree = Graph('Arbre Minimal')
        disj_sets = {}
        nodes = self.nodes

        # File de priorite
        Q = []

        for node in nodes:
            disj_sets[node] = DisjointSet(node)
            heappush(Q, disj_sets[node])

        # Choix de la racine (n'importe quel set)
        if root == "default":
            r = heappop(Q)
        else:
            r = disj_sets[root]

        r.key = 0
        heappush(Q, r)

        while len(Q) > 0:
            u_set = heappop(Q)
            u = u_set.node
            logging.debug("Noeud ajoute a l'arbre minimal : %s", u)
            min_tree.add_node(u)

            if u_set.key is not 0:
                p = u_set.parent.node
                min_tree.add_edge(self.__adj[p][u])

            for v in [w for w in self.__adj[u].keys() if disj_sets[w] in Q\
                    and self.__adj[u][w].weight < disj_sets[w].key]:
                disj_sets[v].parent = u_set
                disj_sets[v].key = self.__adj[u][v].weight

        return min_tree

    def pre_order_traversal(self, root, original_graph):
        """Parcours en pre-ordre retournant la tournee correspondante.
        Attention, la methode ne va fonctionner qu'avec des arbres"""

        # Definition d'une liste que l'on va utiliser comme une pile
        nodes_stack = []

        # Definition du graphe de tournee
        tour_graph = Graph("Tournee approchee")

        #Initialisation
        node = root
        tour_graph.add_node(node)
        logging.debug("Noeud ajoute a la tournee minimale : %s", node)
        sons = self.__adj[node].keys()
        logging.debug("  Fils du noeud courant : %s", sons)

        # Definition d'un dictionnaire pour savoir qui a deja ete visite
        visited = {node_visit: False for node_visit in self.nodes}
        visited[node] = True

        # On empile les fils
        nodes_stack.extend(sons)
        nb_nodes = self.get_nb_edges()

        # Parcours iteratif : tant que la pile est non vide
        while nodes_stack:

            #On depile le prochain noeud et on le marque visite
            next_node = nodes_stack.pop()
            visited[next_node] = True

            # On l'ajoute a la tournee, ainsi que l'arete cree
            tour_graph.add_node(next_node)
            logging.debug("Noeud ajoute a la tournee minimale : %s", next_node)
            edge = original_graph.adj[node][next_node]
            tour_graph.add_edge(edge)

            # On empile les fils du noeud
            sons = [son for son in self.__adj[next_node].keys() if not visited[son]]
            logging.debug("  Fils du noeud courant : %s", sons)
            nodes_stack.extend(sons)
            node = next_node

        # Il reste a ajouter le dernier noeud et boucler la boucle
        edge = Edge(count, node, root)
        tour_graph.add_edge(edge)

        return tour_graph

    def rsl(self,root,algo):
        "Algorithme de Rosenkrantz, Stearns et Lewis"

        # Calcul d'un arbre de recouvrement minimal
        if algo == "prim":
            min_tree = self.prim(root)
        elif algo == "kruskal":
            min_tree = self.kruskal_pp()

        # Exploration de l'arbre en pre-ordre
        min_tour = min_tree.pre_order_traversal(root,self)

        return min_tour

    def plot_graph(self):
        "Representation graphique du graphe avec Matplotlib."

        import matplotlib.pyplot as plt
        from matplotlib.collections import LineCollection

        fig = plt.figure()
        ax = fig.add_subplot(111)

        # Plot nodes
        nodes = self.nodes

        try:
            x = [node.data[0] for node in nodes]
            y = [node.data[1] for node in nodes]

            # Plot edges
            edges = self.edges
            edge_pos = np.asarray([(e.nodes[0].data,
                e.nodes[1].data) for e in edges])
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
        name = self.name
        nb_nodes = self.get_nb_nodes()
        nb_edges = self.get_nb_edges()
        s = 'Graphe %s comprenant %d noeuds et %d aretes' % (name, nb_nodes, nb_edges)

        for node in self.nodes:
            s += '\n  ' + repr(node)

        for edge in self.edges:
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
