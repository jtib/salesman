"""Main TSP hook."""

from tsp_helper import get_distance


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
    nMarks = len(geoPoints)

    # create Graph
    G = Graph(name='Graphe')

    # add edges and nodes to graph
    nb_edges = sum(xrange(nMarks))
    k = 0
    for e in list(its.product(xrange(nb_edges), xrange(nb_edges))):
        n0 = e[0]
        first_node = Node(iden = n0, name='Noeud {}'.format(n0)))
        G.add_node(Node(iden = n0, name='Noeud {}'.format(n0)))
        n1 = e[1]
        second_node = Node(iden = n1, name='Noeud {}'.format(n1)))
        G.add_node(Node(iden = n1, name='Noeud {}'.format(n1)))
        d = getDistance(geoPoints[n0], geoPoints[n1])
        G.add_edge(Edge(iden = k, node1=first_node, node1=second_node,
            weight = d))
        k += 1

    logging.info('Graphe cree')

    # RSL algorithm
    roots = G.nodes
    results = {}
    best = float('inf')
    best_tour = Graph('Best tour')

    for k in xrange(len(roots)):
        min_tour_kruskal = G.rsl(roots[k], "kruskal", "dfs")
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
        neighbors = G.adj[node].keys()
        next_node = neighbors[0] if neighbors[0] is not node else\
                neighbors[1]
        order.append(next_node.id)
        node = next_node

    order.append(order[0])

    return order
