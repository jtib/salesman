if __name__ == "__main__":

    import sys
    import logging
    import matplotlib.pyplot as plt

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

        # Algorithme RSL
        logging.info("Debut de Rosenkrantz")
        roots = G.nodes

        if "bayg29" in finstance:
            min_tour = G.rsl(roots[14],"prim","dfs")
            name = "bayg29_min_tour.png"
        elif "bays29" in finstance:
            min_tour = G.rsl(roots[23],"kruskal","dfs")
            name = "bays29_min_tour.png"
        elif "brazil58" in finstance:
            min_tour = G.rsl(roots[42],"kruskal","dfs")
            name = "brazil58_min_tour.png"
        elif "brg180" in finstance:
            min_tour = G.rsl(roots[2],"prim","dfs")
            name = "brg180_min_tour.png"
        elif "dantzig42" in finstance:
            min_tour = G.rsl(roots[41],"prim","dfs")
            name = "dantzig42_min_tour.png"
        elif "fri26" in finstance:
            min_tour = G.rsl(roots[25],"kruskal","dfs")
            name = "fri26_min_tour.png"
        elif "gr120" in finstance:
            min_tour = G.rsl(roots[78],"kruskal","dfs")
            name = "gr120_min_tour.png"
        elif "gr17" in finstance:
            min_tour = G.rsl(roots[1],"prim","dfs")
            name = "gr17_min_tour.png"
        elif "gr21" in finstance:
            min_tour = G.rsl(roots[0],"kruskal","dfs")
            name = "gr21_min_tour.png"
        elif "gr24" in finstance:
            min_tour = G.rsl(roots[14],"kruskal","dfs")
            name = "gr24_min_tour.png"
        elif "gr48" in finstance:
            min_tour = G.rsl(roots[12],"kruskal","dfs")
            name = "gr48_min_tour.png"
        elif "hk48" in finstance:
            min_tour = G.rsl(roots[6],"kruskal","dfs")
            name = "hk48_min_tour.png"
        elif "swiss42" in finstance:
            min_tour = G.rsl(roots[29],"kruskal","dfs")
            name = "swiss42_min_tour.png"
        elif "pa561" in finstance:
            min_tour = G.rsl(roots[0],"kruskal","dfs")
            name = "pa561_min_tour.png"

        print "Poids : {0}".format(min_tour.tree_weight())
        min_tour.plot_graph(name=name,save=True)

        logging.info('Fin')
