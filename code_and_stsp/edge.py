class Edge(object):
    """
    Une classe generique pour representer les aretes d'un graphe.
    """

    def __init__(self, iden, node1, node2, weight = 0):
      if node1.get_id() == node2.get_id() and weight != 0:
          raise EdgeException('Une arete ne peut pas pointer sur elle-meme.')
      else:
        self.__nodes = (node1, node2)
        self.__weight = weight
        self.__id = iden

    def get_nodes(self):
        "Donne les noeuds."
        return self.__nodes

    def get_weight(self):
        "Donne le poids."
        return self.__weight

    def get_id(self):
        "Donne l'identifiant."
        return self.__id

    def __le__(self, other_edge):
        "Inferieur ou egal : comparaison en fonction du poids"
        return self.__weight <= other_edge.get_weight()

    def __lt__(self, other_edge):
        "Inferieur ou egal : comparaison en fonction du poids"
        return self.__weight < other_edge.get_weight()

    def __repr__(self):
        id = self.get_id()
        weight = self.get_weight()
        nodes = self.get_nodes()
        s  = 'Arete {i} (poids : {p}) '.format(i = id, p = weight)
        s += '({0} <---> {1})'.format(nodes[0].get_id(), nodes[1].get_id())
        return s

class EdgeException(Exception):
    def __init__(self, reason):
        self.__reason = reason
    def __str__(self):
        return self.__reason


if __name__ == '__main__':
    from node import Node
    aretes = []
    n1 = Node(iden=0)
    n2 = Node(iden=1)
    for k in xrange(5):
        aretes.append(Edge(iden = k, node1=n1, node2=n2))
    for arete in aretes:
        print arete




