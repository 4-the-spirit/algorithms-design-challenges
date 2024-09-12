import numpy


def maximize_average_grade(functions, total_hours):
    """
    Question:
    The end of the semester is approaching, and you are required to complete the
    final project for each of the n courses you are taking. Your goal is to achieve
    the maximum average grade across all courses. You have a total of H hours (H > n)
    to allocate to these projects, where H is a positive integer, and the number
    of hours you work on each project must also be an integer.

    For each course i, you are provided with a non-decreasing function f_i(h),
    which estimates the grade you will receive in course i if you dedicate h ≤ H hours
    to its project.

    Given these functions {f_i} and the total time H, design an algorithm that finds
    how many hours to allocate to each project in order to maximize the average grade.
    The algorithm should run in polynomial time with respect to H and n.
    """

    f = functions
    H = total_hours
    n = len(functions)

    opt = numpy.zeros((n + 1, H + 1))
    solution = dict()
    f.insert(0, lambda x: x)

    HOURS_LABEL = "hours"
    AVERAGE_LABEL = "average"

    # Arrays initialization
    for h in range(0, H + 1):
        opt[0, h] = 0

    for i in range(0, n + 1):
        # Calculate the total grade sum if no hours are allocated to any projects.
        total_grades_zero_hours = 0
        for j in range(1, i + 1):
            total_grades_zero_hours += f[j](0)
        opt[i, 0] = total_grades_zero_hours

    # Fill the optimal solutions array, column by column.
    for h in range(1, H + 1):
        for i in range(1, n + 1):
            total_grades_h_hours = 0
            for k in range(0, h + 1):
                total_grades_h_hours = max(total_grades_h_hours, f[i](k) + opt[i - 1, h - k])
            opt[i, h] = total_grades_h_hours

    # Iterate over the array to restore the solution.
    i = n
    h = H

    while i >= 1:
        # Iterate over the array to restore the solution.
        # To find the value of k that leads to the optimal solution,
        # we iterate while i >= 1 (i.e., there are still courses that haven't been assigned hours).
        # After each iteration, update i -= 1 and h -= k.

        hours = list(range(0, h + 1))
        optimal_hour_index = numpy.argmax([(f[i](k) + opt[i - 1, h - k]) for k in hours])
        optimal_hour = hours[optimal_hour_index]
        solution[i] = optimal_hour

        i -= 1
        h -= optimal_hour
    return {HOURS_LABEL: solution, AVERAGE_LABEL: opt[n, H] / n}
