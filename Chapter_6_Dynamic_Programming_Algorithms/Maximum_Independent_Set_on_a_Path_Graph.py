import numpy
import collections
from .utils import SafeArray


def max_independent_set_path(graph_weights):
    """
    Given a path graph G = (V, E), where each node v_i ∈ V has an assigned weight w_i,
    an independent set S ⊆ V is a subset of vertices such that no two vertices in S
    are adjacent (i.e., there is no edge between any two vertices in S).

    The graph G is called a path if its vertices can be labeled as v_1, v_2, ..., v_n,
    such that there is an edge (v_i, v_j) ∈ E if and only if |i - j| = 1,
    meaning each vertex is connected to the next in a sequence.

    This function finds an independent set S in the path graph G such that
    the total weight of the vertices in S is maximized.
    """

    FIRST_VERTEX_INDEX = 0
    SECOND_VERTEX_INDEX = 1

    n = len(graph_weights)
    opt = SafeArray((numpy.zeros(n) - numpy.inf).tolist(), default=0)
    opt[0] = graph_weights[0]
    solution = collections.deque()

    for i in range(1, n):
        opt[i] = max(opt[i-1], graph_weights[i] + opt[i - 2])
    # Restore the solution.
    i = n - 1
    while i >= 0:
        if graph_weights[i] + opt[i - 2] > opt[i - 1]:
            solution.appendleft(i)
            i -= 2
        else:
            i -= 1
    return list(solution)
