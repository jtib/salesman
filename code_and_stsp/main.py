if __name__ == "__main__":

    import sys
    import logging

    from node import Node
    from edge import Edge
    from graph import Graph
    import read_stsp as rs

    logging.basicConfig(filename='logfile.log', level=logging.DEBUG)
    logging.info('Debut')

    finstance = sys.argv[1]

    with open(finstance, 'r') as fd:

        header = rs.read_header(fd)
        dim = header['DIMENSION']
        edge_weight_format = header['EDGE_WEIGHT_FORMAT']

        nodes = rs.read_nodes(header, fd)
        edges = rs.read_edges(header, fd)

        # create Graph
        G = Graph(name='Graphe')

        # convert dim
        dim = int(dim)

        # add nodes to graph
        if len(nodes) == 0:
            nodes = {k:None for k in xrange(dim)}
        for node in nodes.items():
            # node id
            n = node[0]
            # node data
            d = node[1]
            G.add_node(Node(iden = n, name='Noeud {}'.format(n), data=d))

        # add edges to graph
        nb_edges = sum(xrange(dim))
        K=0
        for edge in edges:
            # nodes
            (nid1, nid2) = (edge[0], edge[1])
            node_list = G.retrieve_nodes_from_id(nid1, nid2)
            n1 = node_list[0]
            n2 = node_list[0] if len(node_list)==1 else node_list[1]
            # weight
            w = edge[2]
            # edge id
            # add edge if not circular
            if not(w==0 and n1==n2):
                G.add_edge(Edge(iden = K, node1=n1, node2=n2, weight=w))
                K += 1

        logging.info('Fichier lu, graphe cree')

        #print G
        #G.plot_graph()

        # Kruskal's algorithm
        #logging.info("Debut de l'algorithme de Kruskal")
        #min_tree = G.kruskal()
        #print min_tree
        #min_tree.plot_graph()

        # # Kruskal improved
        # logging.info('Kruskal improved')
        # min_tree_pp = G.kruskal_pp()
        # print min_tree_pp
        # # min_tree_pp.plot_graph()
        #
        # # Prim's algorithm
        # logging.info("Debut de Prim")
        # min_tree_prim = G.prim()
        # print min_tree_prim
        # # min_tree_prim.plot_graph()

        # Algorithme RSL
        logging.info("Debut de Rosenkrantz")
        roots = G.nodes
        min_tour = G.rsl(roots[0],"prim","dfs")
        print min_tour.tree_weight()

        logging.info('Fin')
