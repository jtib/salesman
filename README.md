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

##### Lab 2
* respecter le guide de style
* exemples dans livre Cormen pour prochain lab
* méthodes en petites capitales dans instructions
* possibilités : faire une classe DisjointSet et lui ajouter les méthodes en question,
ou ajouter attribut "parent" à la classe Node et lui ajouter ces mêmes méthodes (ce qui élimine un objet mais est moins rigoureux)
* 23.2 - The algorithms of Kruskal and Prim (p.631)
* représentation visuelle des graphes : utile pour le débogage
