import numpy
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

    n = len(graph_weights)
    opt = SafeArray((numpy.zeros(n) - numpy.inf).tolist(), default=0)
    opt[0] = 0
    opt[1] = graph_weights[0]
    solution = SafeArray([], default=-1)

    for i in range(2, n):
        opt[i] = max(opt[i-1], graph_weights[i] + opt[i - 2])
        # Restore the solution.
        if graph_weights[i] + opt[i - 2] > opt[i - 1]:
            # If the optimal solution contains the last vertex v_i,
            # we cannot include vertex v_(i-1) in it, if it's already included.
            if solution[-1] == i-1:
                solution.pop()
            solution.append(i)
    # If the second vertex is not part of the optimal solution and
    # the first vertex contributes to the total weight, we will include
    # the first vertex in the solution.
    if solution[0] != 2 and opt[1] + opt[n-1] > opt[n-1]:
        solution.appendleft(1)
    return solution

