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
        self.__adj.setdefault(node,{None : None})

    def add_edge(self, edge):
        "Ajoute une arete au graphe."
        (n1,n2) = edge.get_nodes()
        if n1 in self.__adj.keys():
            self.__adj[n1][n2] = edge
        else:
            self.add_node(n1)
            self.__adj[n1] = {n2:edge}
        if n2 in self.__adj.keys():
            self.__adj[n2][n1] = edge
        else:
            self.add_node(n2)
            self.__adj[n2] = {n1:edge}

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
            print type(sd)
            # this is an edge
            e = sd.itervalues().next()
            print e
            # there might not be any edges yet
            if e == None:
                return 0
            else:
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
    for k in range(5):
        #G.add_node(Node(name='test %d' % k))
        n1 = Node(name='test')
        n2 = Node(name='test')
        G.add_edge(Edge(n1,n2,weight=42))

    print G
