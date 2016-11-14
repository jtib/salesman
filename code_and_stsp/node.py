class Node(object):
    """
    Une classe generique pour representer les noeuds d'un graphe.
    """

    def __init__(self, iden, name='Sans nom', data=None, rank=0):
        self.__name = name
        self.__data = data
        self.__id = iden
        self.__rank = rank

    def get_name(self):
        "Donne le nom du noeud."
        return self.__name

    def get_id(self):
        "Donne le numero d'identification du noeud."
        return self.__id

    def get_data(self):
        "Donne les donnees contenues dans le noeud."
        return self.__data

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, value):
        self.__key = value

    def __lt__(self, other_node):
        return self.key < other_node.key

    def __le__(self, other_node):
        return self.key <= other_node.key

    def __repr__(self):
        id = self.get_id()
        name = self.get_name()
        data = self.get_data()
        s  = '%s (id %d)' % (name, id)
        s += ' (donnees: ' + repr(data) + ')'
        return s


if __name__ == '__main__':

    nodes = []
    for k in range(5):
        nodes.append(Node(iden = k))

    for node in nodes:
        print node
