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
            self.__adj[n1] = {n2,edge}
        if n2 in self.__adj.keys():
            self.__adj[n2][n1] = edge
        else:
            self.add_node(n2)
            self.__adj[n2] = {n1,edge}

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
        else return self.__adj.iterkeys().next().get_count()

    def get_edges(self):
        "Donne la liste des aretes du graphe."
        edges = []
        edges.extend([v for n in self.get_nodes() for v in self.__adj[node].values()])
        return list(set(edges)) # removing doubles


    def __repr__(self):
        name = self.get_name()
        nb_nodes = self.get_nb_nodes()
        s = 'Graphe %s comprenant %d noeuds' % (name, nb_nodes)
        for node in self.get_nodes():
            s += '\n  ' + repr(node)
        return s


if __name__ == '__main__':

    from node import Node

    G = Graph(name='Graphe test')
    for k in range(5):
        G.add_node(Node(name='Noeud teste %d' % k))

    print G
