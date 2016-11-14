import logging
from node import Node

class DisjointSet(object):
    """
    Classe pour representer un sous-arbre dans un ensemble disjoint
    """

    def __init__(self, node):
        self.__node = node
        # Le noeud est une racine par defaut
        # Le parent est de type disjoint set
        self.__parent = None
        self.__rank = 0

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
        self.__parent = val

    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, value):
        self.__rank = value

    def union_sets(self,dset):
        """Realise l'union de deux sous ensembles disjoints par leurs racines.
        Renvoie True si l'union est possible, False si les deux ensembles sont connexes
        """
        root1 = self.find_root()
        root2 = dset.find_root()

        if root1 != root2:
            root2.parent = root1
            return True
        else:
            return False

    def rank_compressed_union(self,dset):
        """Realise l'union par le rang de deux sous-ensembles disjoints avec compression des chemins.
        Renvoie True si l'union est possible, False si les deux ensembles sont connexes
        """

        root1 = self.find_root()
        root2 = dset.find_root()

        # si les ensembles sont connexes
        if root1 == root2:
            return False
        # sinon
        if root1.rank > root2.rank:
            root2.parent = root1
            dset.parent = root1
        elif root1.rank < root2.rank:
            root1.parent = root2
            self.__parent = root2
        elif root1.rank == root2.rank:
            root1.parent = root2
            self.__parent = root2
            root2.rank += 1
        return True

    def find_root(self):
        "Renvoie la racine de l'ensemble"
        # Si l'element courant est la racine
        if self.__parent == None:
            return self
        # Sinon on applique la methode au parent
        return self.__parent.find_root()

    def __repr__(self):
        "Affiche les identifiants des noeuds jusqu'a la racine"
        s = '%d' % self.__node.get_id()
        if self.__parent == None:
            return s + " = racine."
        s += ' --> ' + str(self.__parent)
        return s


if __name__ == '__main__':
    # Creation de trois noeuds et des trois ensembles disjoints associes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    set1 = DisjointSet(node1)
    set2 = DisjointSet(node2)
    set3 = DisjointSet(node3)
    # set2 devient la racine de set1
    set1.parent = set2
    print set1

    # On affiche la racine de set1
    print set1.find_root()

    # On essaye d'unir deux membres d'un meme ensemble
    print set1.union_sets(set2)

    # On unit deux ensembles disjoints et on verifie le booleen de sortie
    print set1.union_sets(set3)
    # On affiche les trois sous-ensembles initiaux
    print set1, set2, set3

    set1 = DisjointSet(node1)
    set2 = DisjointSet(node2)
    set3 = DisjointSet(node3)

    print set1.rank_compressed_union(set2)
    print set1.rank_compressed_union(set3)

    # On affiche les trois sous-ensembles initiaux
    print set1, set2, set3
