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
    print "fist leg length: ", get_distance(geoPoints[0], geoPoints[1])
    order = range(nMarks)  # default order
    order = order + [order[0]]
    return order
