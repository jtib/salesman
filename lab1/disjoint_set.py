class DisjointSet(object):
    """
    Classe pour representer un sous-arbre dans un ensemble disjoint
    """

    def __init__(self, node):
        self.__node = node
        # Le noeud est une racine par defaut
        # Le parent est de type disjoint set
        self.__parent = None

    @property
    def node(self):
        "Accesseur du noeud courant"
        return self.__node

    @node.setter
    def node(self,val):
        "Pas de modification possible du noeud courant"
        raise AttributeError("Le noeud courant n'est pas modifiable directement")

    @property
    def parent(self):
        "Accesseur du noeud parent"
        return self.__parent

    @parent.setter
    def parent(self,val):
        "Modification du parent"
        # Mettre les verifications
        if self.__parent == None:
            self.__parent = val
        #A compléter



