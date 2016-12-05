"""Main TSP hook."""

import sys
import logging

from tsp_helper import get_distance
import itertools as its
from graph import Graph
from node import Node
from edge import Edge

def get_visit_order(geoPoints):
    """THIS IS THE ONLY FUNCTION THAT YOU NEED TO MODIFY FOR PHASE 5.

    The only argument, *geoPoints*, is a list of points that user has marked.
    Each element of geoPoints is an instance of the GeoPoint class. You need to
    create your graph using these points. You obtain the distance between two
    points by calling the *getDistance* function; for example:

    get_distance(geoPoints[0], geoPoints[1])

    Run your tsp solver and return the locations visit order. The return value,
    *order*, must be a list of indices of points, specifying the visit order.

    In the example implementation below, we visit each point by the order
    in which they were marked (clicked).
    """
    logging.basicConfig(filename='logfile.log', level=logging.DEBUG)
    logging.info('Beginning get_visit_order')

    nMarks = len(geoPoints)

    # create Graph
    G = Graph(name='Graphe')

    # add nodes to graph
    for n in xrange(nMarks):
        G.add_node(Node(iden = n, name = 'Noeud {}'.format(n)))

    # add edges to graph
    k = 0
    for e in its.combinations(xrange(nMarks), 2):
        # nodes
        (nid1, nid2) = (e[0], e[1])
        node_list = G.retrieve_nodes_from_id(nid1, nid2)
        n1 = node_list[0]
        n2 = node_list[1]
        # weight
        d = get_distance(geoPoints[nid1], geoPoints[nid2])
        G.add_edge(Edge(iden = k, node1=n1, node2=n2, weight = d))
        k += 1

    logging.info('Graphe cree')

    # RSL algorithm
    roots = G.nodes
    results = {}
    best = float('inf')
    best_tour = Graph('Best tour')

    for k in xrange(len(roots)):
        logging.debug('Debut de Kruskal')
        min_tour_kruskal = G.rsl(roots[k], "kruskal", "dfs")
        logging.debug('Debut de Prim')
        min_tour_prim = G.rsl(roots[k], "prim", "dfs")
        results[k] = {min_tour_kruskal.tree_weight(): 'kruskal',
                min_tour_prim.tree_weight(): 'prim'}

        if min(results[k]) < best:
            best = min(results[k])
            best_alg = results[k][min(results[k])]
            best_tour = min_tour_prim if best_alg is 'prim' else\
                    min_tour_kruskal

    # Best order
    node = best_tour.nodes[0]
    order = [node.id]

    while len(order) < len(best_tour.nodes):
        neighbors = best_tour.adj[node].keys()
        next_node = neighbors[0] if neighbors[0].id not in order else\
                neighbors[1]
        order.append(next_node.id)
        node = next_node

    order.append(order[0])

    logging.debug('order = %s', order)

    return order
