import numpy
import collections
from .utils import SafeArray


def schedule_tasks_for_max_earnings(high, low):
    """
    Question:
    We manage a team of Software Engineers, and each week we must assign them a task
    for execution. The tasks range in difficulty: easier tasks include bug fixes for
    clients and software testing, while more challenging ones involve software design
    and implementing complex algorithms.

    In any given week i, we can assign an easy task, which will yield a reward of
    low_i > 0, or a difficult task, which will yield high_i > 0. However, if we assign
    a difficult task in week i, the team must rest during week i-1, meaning no tasks
    (easy or difficult) can be executed in the prior week.

    Given a series of n weeks, we need to decide which tasks to assign in each week,
    maximizing the total earnings while adhering to these constraints.
    """

    n = len(high)
    opt = SafeArray(numpy.zeros(n), default=0)
    opt[0] = max(high[0], low[0])
    solution = collections.deque()

    DIFFICULT_TASK_LABEL = "difficult"
    EASY_TASK_LABEL = "easy"

    for i in range(1, n):
        opt[i] = max(high[i] + opt[i-2], low[i] + opt[i-1])
    # Restore the solution.
    i = n - 1
    while i >= 0:
        if high[i] + opt[i-2] > low[i] + opt[i-1]:
            solution.appendleft((DIFFICULT_TASK_LABEL, i))
            # If the optimal solution for the current challenge includes a difficult task
            # in the final week, we cannot select any task in the previous week.
            i -= 2
        else:
            solution.appendleft((EASY_TASK_LABEL, i))
            i -= 1
    return list(solution)
