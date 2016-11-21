class Node(object):
    """
    Une classe generique pour representer les noeuds d'un graphe.
    """

    def __init__(self, iden, name='Sans nom', data=None):
        self.__name = name
        self.__data = data
        self.__id = iden

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def data(self):
        "Donne les donnees contenues dans le noeud."
        return self.__data

    def __repr__(self):
        id = self.id
        name = self.name
        data = self.data
        s  = '%s (id %d)' % (name, id)
        s += ' (donnees : ' + repr(data) + ')'
        return s


if __name__ == '__main__':

    nodes = []
    for k in range(5):
        nodes.append(Node(iden = k))

    for node in nodes:
        print node
