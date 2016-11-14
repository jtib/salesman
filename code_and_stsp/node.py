from sys import maxsize

class Node(object):
    """
    Une classe generique pour representer les noeuds d'un graphe.
    """

    def __init__(self, iden, name='Sans nom', data=None, key=maxsize):
        self.__name = name
        self.__data = data
        self.__id = iden
        self.__key = key

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
        id = self.id
        name = self.name
        data = self.data
        key = self.key
        s  = '%s (id %d)' % (name, id)
        s += ' (donnees : ' + repr(data) + ')'
        s += ' (clef : ' + repr(key) + ')'
        return s


if __name__ == '__main__':

    nodes = []
    for k in range(5):
        nodes.append(Node(iden = k))

    for node in nodes:
        print node
