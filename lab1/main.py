if __name__ == "__main__":

    import sys

    from node import Node
    from edge import Edge
    from graph import Graph
    import read_stsp as rs

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
        for (e, edge) in zip(xrange(nb_edges), edges):
            # nodes
            (n1, n2) = (edge[0], edge[1])
            # weight
            w = edge[2]
            # edge id
            G.add_edge(Edge(iden = e, node_id1=n1, node_id2=n2, weight=w))

        print G
