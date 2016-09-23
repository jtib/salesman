class Edge(object):
    """
    Une classe generique pour representer les aretes d'un graphe.
    """

    __edge_count = -1 # Compteur global partage par toutes les instances.

    def __init__(self, node1, node2, weight = 0):
      self.__nodes = (node1, node2)
      self.__weight = weight
      Edge.__edge_count += 1
      self.__id = Edge.__edge_count

    def get_nodes(self):
        "Donne les noeuds."
        return self.__nodes

    def get_weight(self):
        "Donne le poids."
        return self.__weight

    def get_id(self):
        "Donne l'identification."
        return self.__id

    def __repr__(self):
        id = self.get_id()
        weight = self.get_weight()
        nodes = self.get_nodes()
        s  = 'Arete {i} (poids : {p}) '.format(i = id, p = weight)
        s += '(noeuds : ' + repr(nodes[0]) + ', ' + repr(nodes[1])
        return s

if __name__ == '__main__':

    from node import Node
    n1 = Node()
    n2 = Node()

    aretes = []
    for k in xrange(5):
        aretes.append(Edge(node1 = n1, node2 = n2))

    for arete in aretes:
        print arete

