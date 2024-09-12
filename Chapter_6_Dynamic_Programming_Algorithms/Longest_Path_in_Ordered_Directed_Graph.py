import numpy
import collections


def find_longest_path(ordered_directed_graph):
    """
    Question:
    Let G = (V, E) be a directed graph with vertices v_1, v_2, ..., v_n.
    We say that G is an ordered graph if for each edge (v_i, v_j) ∈ E, the following holds: i < j.
    Additionally, for each vertex v_i ∈ V (except v_n), there exists an edge (v_i, v_j) ∈ E.

    Given an ordered graph G, design an algorithm to find the longest path
    that starts at v_1 and ends at v_n.
    """

    n = len(ordered_directed_graph.nodes)
    # Includes the initialization of opt[0] and opt[1]
    opt = numpy.zeros(n + 1)
    decisions = []
    solution = collections.deque()

    for i in range(2, n + 1):
        opt[i] = (-1) * numpy.inf
        # Iterate over the edges entering vertex v_i and find the one
        # that maximizes the expression opt[j], where 1 <= j <= i,
        # as the graph is ordered.
        in_edges = ordered_directed_graph.in_edges(i)
        if len(in_edges) == 0:
            continue

        possible_source_vertices = [edge[0] for edge in in_edges]
        optimal_source_solutions = [opt[j] for j in possible_source_vertices]
        maximizing_vertex_index = numpy.argmax(optimal_source_solutions)
        maximizing_vertex_solution = optimal_source_solutions[maximizing_vertex_index]

        if maximizing_vertex_solution > (-1) * numpy.inf:
            opt[i] = 1 + maximizing_vertex_solution
            decisions.append((possible_source_vertices[maximizing_vertex_index], i))

    # Reconstruct the solution based on the decisions made,
    # starting from the final decision that led to vertex v_n.
    last_edge = decisions[-1]
    last_edge_src = last_edge[0]
    last_edge_dest = last_edge[1]
    solution.appendleft(last_edge)

    for i in range(len(decisions) - 1, -1, -1):
        current_edge = decisions[i]
        current_edge_src = current_edge[0]
        current_edge_dest = current_edge[1]

        if current_edge_dest == last_edge_src:
            last_edge_src = current_edge_src
            last_edge_dest = current_edge_dest
            solution.appendleft((last_edge_src, last_edge_dest))
    return list(solution)
