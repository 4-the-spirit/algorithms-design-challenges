import numpy
import collections


def optimize_matrix_multiplication(dimensions):
    """
    Question:
    The multiplication of a matrix series A_1 x A_2 x ... x A_n is only valid
    when the dimensions match correctly. Specifically, if r_i represents the
    number of rows in matrix A_i, and c_i represents its number of columns,
    then for the multiplication to be valid, it must hold that c_i = r_{i+1}
    for all 1 <= i < n.

    When A_i x A_(i+1) is computed, the resulting matrix has r_i rows and
    c_{i+1} columns, and the time complexity of the multiplication is
    Θ(r_i x c_i x c_{i+1}) operations.

    Since matrix multiplication is associative, parentheses can be placed
    in any order, such as (A_1 x A_2) x A_3 or A_1 x (A_2 x A_3). The order
    in which the matrices are multiplied can greatly affect the total number
    of operations required.

    Design an algorithm that, given a list of matrix dimensions
    [(r_1, c_1), (r_2, c_2), ..., (r_n, c_n)], finds the optimal way to
    parenthesize the matrix chain multiplication to minimize the number of
    operations.
    """

    row = [dim[0] for dim in dimensions]
    col = [dim[1] for dim in dimensions]

    n = len(dimensions)
    opt = numpy.zeros((n, n)) + numpy.inf
    decisions = dict()
    solution = dict()

    PARENTHESES_ORDER_LABEL = "order"
    SOLUTION_VALUE_LABEL = "value"

    # Array initialization.
    for k in range(0, n):
        opt[k, k] = 0

    # Fill the diagonals of the optimal solutions array one after another.
    for diff in range(1, n):
        for i in range(0, n - diff):
            j = i + diff
            minimizing_matrix = i
            for k in range(i, j):
                optimal_num_of_operations_with_k_in_middle = opt[i, k] + opt[k + 1, j] + row[i] * col[k] * col[j]
                if optimal_num_of_operations_with_k_in_middle < opt[i, j]:
                    opt[i, j] = optimal_num_of_operations_with_k_in_middle
                    minimizing_matrix = k
            decisions.update({(i, j): minimizing_matrix})
    i = 0
    j = n - 1
    queue = collections.deque([(i, j)])
    # We start with the final solution, and extract its minimizing matrix 'k' in each iteration.
    # By finding 'k' we are required to exam the 'k' of the optimal solutions that our current
    # optimal solution is built with: opt(i,k), opt(k+1,j).
    while len(queue) != 0:
        element = queue.pop()
        i = element[0]
        j = element[1]
        out_of_bounds = (i < 0 or j < 0 or i > j)
        single_matrix_mult = (i == j)

        if out_of_bounds or single_matrix_mult:
            continue

        k = decisions[element]
        solution[element] = k

        # Add the optimal solutions that compose our solution to retrieve their 'k' values.
        queue.appendleft((i, k))
        queue.appendleft((k + 1, j))
    return {PARENTHESES_ORDER_LABEL: solution, SOLUTION_VALUE_LABEL: opt[0, n - 1]}
