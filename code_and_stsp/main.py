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
            (nid1, nid2) = (edge[0], edge[1])
            node_list = G.retrieve_nodes_from_id(nid1, nid2)
            n1 = node_list[0]
            n2 = node_list[0] if len(node_list)==1 else node_list[1]
            # weight
            w = edge[2]
            # edge id
            G.add_edge(Edge(iden = e, node1=n1, node2=n2, weight=w))

        # print G

        # Kruskal's algorithm
        # Each vertex corresponds to a set
        dj_sets = G.sets_from_nodes()
        # Empty set of "selected" edges
        sel_edges = set()
        # Sort the edges in increasing weight order
        edges = G.sort_edges()
        # last part
        for edge in edges:
            (node1, node2) = edge.get_nodes()
            set1 = next(s for s in dj_sets if s.node == node1)
            set2 = next(s for s in dj_sets if s.node == node2)
            (root1, root2) = (set1.find_root(), set2.find_root())
            # if the nodes are in distinct components
            if root1 != root2:
                sel_edges.add(edge)
                set1.union_sets(set2)

        print "\n".join([str(s) for s in dj_sets])
        print "\n".join([str(e) for e in sel_edges])





