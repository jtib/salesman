from node import Node

class Graph(object):
    """
    Une classe generique pour representer un graphe comme un ensemble de
    noeuds.
    """

    def __init__(self, name='Sans nom'):
        self.__name = name
        self.__adj = {} # Matrice d'adjacence

    def add_node(self, node):
        "Ajoute un noeud au graphe."
        self.__adj.setdefault(node,{})

    def add_edge(self, edge):
        "Ajoute une arete au graphe."
        (n1, n2) = edge.get_nodes()
        # retrieving nodes from ids
        nodes = [node for node in self.__adj.keys() if node.get_id() == n1\
                or node.get_id() == n2]
        # if both nodes already there
        if len(nodes) == 2:
            self.__adj[nodes[1]][nodes[0]] = self.__adj[nodes[0]][nodes[1]]\
                    = edge
        # if only one is there and it doesn't point at itself, or none are
        elif len(nodes) < 2 and n1 != n2:
            raise KeyError("Missing node(s). Add all nodes before adding edges\
                (nodes = {0}, n1 = {1}, n2 = {2})".format(nodes, n1, n2))

    def get_name(self):
        "Donne le nom du graphe."
        return self.__name

    def get_nodes(self):
        "Donne la liste des noeuds du graphe."
        return self.__adj.keys()

    def get_nb_nodes(self):
        "Donne le nombre de noeuds du graphe."
        if self.__adj == {}:
            return 0
        # else access random element and get node count
        else:
            return self.__adj.iterkeys().next().get_count()+1

    def get_edges(self):
        "Donne la liste des aretes du graphe."
        edges = []
        edges.extend([v for n in self.get_nodes() for v in self.__adj[n].values()])
        return list(set(edges)) # removing doubles

    def get_nb_edges(self):
        "Donne le nombre d'aretes du graphe."
        if self.__adj == {}:
            return 0
        else:
            # this is a subdictionary
            sd = self.__adj.itervalues().next()
            # there might not be any edges yet
            if sd == {}:
                return 0
            else:
                # this is an edge
                e = sd.itervalues().next()
                return e.get_count()+1

    def __repr__(self):
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
        G.add_node(Node(name='test %d' % count))
        n1 = count
        count += 1
        G.add_node(Node(name='test %d' % count))
        n2 = count
        count += 1
        G.add_edge(Edge(n1, n2, weight=42))
    print G
