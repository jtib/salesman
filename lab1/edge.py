class Edge(object):
    """
    Une classe generique pour representer les aretes d'un graphe.
    """
    #__edge_count = -1 # Compteur global partage par toutes les instances.

    def __init__(self, iden, node_id1, node_id2, weight = 0):
      if node_id1 == node_id2 and weight != 0:
          raise EdgeException('Une arete ne peut pas pointer sur elle-meme.')
      else:
        self.__nodes = (node_id1, node_id2)
        self.__weight = weight
        #Edge.__edge_count += 1
        self.__id = iden

    def get_nodes(self):
        "Donne les identifiants des noeuds."
        return self.__nodes

    def get_weight(self):
        "Donne le poids."
        return self.__weight

    def get_id(self):
        "Donne l'identifiant."
        return self.__id

    def __repr__(self):
        id = self.get_id()
        weight = self.get_weight()
        nodes = self.get_nodes()
        s  = 'Arete {i} (poids : {p}) '.format(i = id, p = weight)
        s += '(noeuds : {0}, {1})'.format(nodes[0], nodes[1])
        return s


class EdgeException(Exception):
    def __init__(self, reason):
        self.__reason = reason

    def __str__(self):
        return self.__reason


if __name__ == '__main__':
    from node import Node
    aretes = []
    for k in xrange(5):
        aretes.append(Edge(iden = k, node_id1 = 0, node_id2 = 1))
    for arete in aretes:
        print arete



