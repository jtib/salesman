## MTH6412B - Project
### A solution to the travelling salesman problem

##### Notes sur les remises :
* remettre un fichier pdf (le rapport) et une archive zip (pas d'autre format de compression) contenant le code
* deuxième chose : avoir un programme principal à faire tourner pour pouvoir reproduire les résultats inscrits dans le rapport. Les résultats doivent bien sûr être les mêmes, et surtout ne pas faire de choses stupides comme inventer des résultats sans le code qui correspond... Prévenir dans le rapport si telle ou telle chose ne marche pas + écrire ce qui a été essayé.
* Le code déjà remis peut être modifié plus tard dans le projet.

##### Lab 0
* mail Maxime : maxime.mcl@gmail.com
* Intro to algorithms (Cormen)
* Learning Python (Lutz & Ascher)
* Debugger? (inclus dans pycharm...)
* matplotlib pour figures graphes

##### Lab 1
* installer pip [pas nécessaire, déjà là]
* virtualenv? [non, pas avec conda]
* lire Cormen 22.1 [fait]
* attribut poids, nœud départ/fin arête, numéro d'identification pour node
* matrice d'adjacence : double dictionnaire, p.ex. ({node1:{node2:edge}})
* autre possibilité : node.adj = [], avec [] = liste des nœuds adjacents à node
* mais plus élégant d'utiliser des dictionnaires, plus efficace, et moins de
risques d'erreurs [donc dico]
* méthode print() associée à la classe graphe : incorporer arêtes dans print()
=> idée = dans une méthode print(), appeler celle de l'objet (ds graph.print(),
appelle node.print() ; nous = rajouter edge.print())
* dans readstsp, fonction appelée plotgraph. La mettre dans graph
* faire programme de test pour vérifier que tout fonctionne
* attention : la lecture des edges fournie les prend ss forme de str, pas de
float/int
* avoir compteur pour nodes et edge (cf. len(), qui doit parcourir la liste au
complet à chaque fois... donc mieux d'avoir un compteur)
* certains pbs associent des coordonnées aux nœuds, d'autres non, mais tous
doivent être résolus, donc ne pas s'occuper des coordonnées (qui ne servent
éventuellement que pr l'affichage)
* add_edge et adjacence (matrice) (étendre classe edge)
* Lien du rapport : [https://www.overleaf.com/6323837bfwnry](https://www.overleaf.com/6323837bfwnry)

##### Lab 2
* respecter le guide de style
* exemples dans livre Cormen pour prochain lab
* méthodes en petites capitales dans instructions
* possibilités : faire une classe DisjointSet et lui ajouter les méthodes en question,
ou ajouter attribut "parent" à la classe Node et lui ajouter ces mêmes méthodes (ce qui élimine un objet mais est moins rigoureux)
* 23.2 - The algorithms of Kruskal and Prim (p.631)
* représentation visuelle des graphes : utile pour le débogage
* utiliser les nodes et pas les id dans les aretes (nooon...)
* mettre des décorateurs
* inclure dossier stsp dans .zip
* Lien du rapport : [https://www.overleaf.com/6629553cxwsxs](https://www.overleaf.com/6629553cxwsxs)

##### Lab 3
* référence dans le livre de Cormen : sections 21.3 et 23
* question théorique sur la complexité : raisonnement par induction
* pseudo-code fourni incomplet, ne construit pas l'arbre au fil des itérations
* possible de modifier les objets Node directement ou implémenter une classe basée sur les nœuds avec de nouveaux attributs
* comparer Kruskal avec Prim (et corriger le problème avec l'ajout des arêtes noté dans les commentaires du lab 2)
* Lien du rapport : [https://www.overleaf.com/6821243wdvbygyrhwkz#/](https://www.overleaf.com/6821243wdvbygyrhwkz#/)

##### Lab 4
* alternatives conseillées : depth-first search itérative en gardant la trace de l'ordre suivi
* ajouter chaque nœud dans le graphe
* ajouter chaque arête entre 2 voisins
* Kruskal ou Prim : passer tous les nœuds comme source pour trouver la meilleure
* dans le rapport :

| Instance | Kruskal | Source | Prim | Source | Écart à optimal (cf. site) |
| -------- | ------- | ------ | ---- | ------ | -------------------------- |
| bayg29.tsp | poids | 55 | poids | 55 | écart |

* site pour les poids optimaux : [http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/STSP.html](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/STSP.html)

##### Lab 5
* interface google maps : graphique, il suffit de cliquer
* six nœuds
* Kruskal ou Prim, peu importe
* utiliser (comme d'habitude) un environnement virtuel pour ne pas avoir de problèmes avec les packages externes
* _seul_ fichier à modifier : my\_tsp.py
* résoudre avec Prim ou Kruskal pour tous les nœuds, puis prendre la meilleure tournée et la retourner
