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

        # add nodes to graph
        for node in nodes.items():
            # node id
            n = node[0]
            # node data
            d = node[1]
            G.add_node(Node(name='Noeud {}'.format(n), data=d))

        # add edges to graph
        for edge in edges:
            # nodes
            (n1, n2) = (edge[0], edge[1])
            # weight
            w = edge[2]
            G.add_edge(Edge(node_id1=n1, node_id2=n2, weight=w))

        print G
