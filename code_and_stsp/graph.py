from node import Node

class Graph(object):
    """
    Une classe generique pour representer un graphe comme un ensemble de
    noeuds.
    """

    def __init__(self, name='Sans nom'):
        self.__name = name
        self.__adj = {} # Matrice d'adjacence
        self.__edges = 0
        self.__nodes = 0


    def get_name(self):
        "Donne le nom du graphe."
        return self.__name


    def get_nodes(self):
        "Donne la liste des noeuds du graphe."
        return self.__adj.keys()


    def get_edges(self):
        "Donne la liste des aretes du graphe."
        edges = []
        edges.extend([v for n in self.get_nodes() for v in self.__adj[n].values()])
        return list(set(edges)) # removing doubles


    def get_nb_nodes(self):
        "Donne le nombre de noeuds du graphe."
        return self.__nodes


    def get_nb_edges(self):
        "Donne le nombre d'aretes du graphe."
        return self.__edges


    def retrieve_nodes_from_id(self, *ids):
        return [node for node in self.__adj.keys()
                if node.get_id() in ids]


    def add_node(self, node):
        "Ajoute un noeud au graphe."
        self.__adj.setdefault(node,{})
        self.__nodes += 1


    def add_edge(self, edge):
        "Ajoute une arete au graphe."
        (n1, n2) = edge.get_nodes()
        # retrieving nodes
        nodes = self.retrieve_nodes_from_id(n1.get_id(), n2.get_id())

        # if both nodes already there
        if len(nodes) == 2:
            self.__adj[nodes[1]][nodes[0]] = self.__adj[nodes[0]][nodes[1]]\
                    = edge
            self.__edges = edge.get_id() + 1 #valid for all tsps, avoids has_key

        # if only one is there and it doesn't point at itself, or none are
        elif len(nodes) < 2 and n1 != n2:
            raise KeyError("Missing node(s). Add all nodes before adding edges\
                (nodes = {0}, n1 = {1}, n2 = {2})".format(nodes, n1.get_id(), n2.get_id()))

    def sort_edges(self):
        "Trie les aretes selon leur poids en ordre croissant."
        edges = self.get_edges()
        edges.sort(key=lambda edge: edge.get_weight())
        return edges


    def __repr__(self):
        "Affiche le graphe."
        name = self.get_name()
        nb_nodes = self.get_nb_nodes()
        nb_edges = self.get_nb_edges()

        s = 'Graphe %s comprenant %d noeuds et %d aretes' % (name, nb_nodes, nb_edges)
        for node in self.get_nodes():
            s += '\n  ' + repr(node)
        for edge in self.get_edges():
            s += '\n  ' + repr(edge)
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
        G.add_edge(Edge(k, n1, n2, weight=k%3))
    print G
    print "Aretes triees par poids :"
    edg = G.sort_edges()
    print "\n".join([str(e) for e in edg])