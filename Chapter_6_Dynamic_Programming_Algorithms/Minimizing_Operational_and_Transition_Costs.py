import numpy
import collections


def find_minimum_cost_plan(new_york_costs, san_francisco_costs, transition_cost):
    """
    Question:
    You are managing a consulting company with clients on both the East and West Coasts.
    Each month, you can choose to operate your business from either the New York office or the San Francisco office.
    If you run the business from New York in month i, your operational cost will be N_i.
    If you run it from San Francisco, the cost will be S_i.

    If you decide to switch from one city to the other between consecutive months (i.e., between month i and month i+1),
    there will be a fixed transition cost of M.

    The total cost of a plan is the sum of the monthly operational costs and any transition costs incurred from switching offices.
    Given the transition cost M, and the series of operational costs N_1, N_2, ..., N_n for New York and S_1, S_2, ..., S_n for San Francisco,
    design a plan that minimizes the total cost.
    """

    n = len(new_york_costs)
    opt_new_york = numpy.zeros(n)
    opt_san_francisco = numpy.zeros(n)

    # Arrays Initialization.
    opt_new_york[0] = new_york_costs[0]
    opt_san_francisco[0] = san_francisco_costs[0]
    solution = collections.deque()

    NEW_YORK_LABEL = "NY"
    SAN_FRANCISCO_LABEL = "SF"
    CITY_LABEL = "city"
    WEEK_LABEL = "week"

    NY_TO_NY_INDEX = 0
    SF_TO_NY_INDEX = 1
    SF_TO_SF_INDEX = 0
    NY_TO_SF_INDEX = 1

    for i in range(1, n):
        opt_new_york[i] = min(new_york_costs[i] + opt_new_york[i - 1],
                              new_york_costs[i] + opt_san_francisco[i - 1] + transition_cost)
        opt_san_francisco[i] = min(san_francisco_costs[i] + opt_san_francisco[i - 1],
                                   san_francisco_costs[i] + opt_new_york[i - 1] + transition_cost)

    # Restore the solution.
    current_city = None
    i = n - 1

    if opt_new_york[i] < opt_san_francisco[i]:
        current_city = NEW_YORK_LABEL
    else:
        current_city = SAN_FRANCISCO_LABEL
    solution.appendleft({CITY_LABEL: current_city, WEEK_LABEL: i + 1})

    while i > 0:
        # Determine the city from which we arrived at the current city.
        if current_city == NEW_YORK_LABEL:
            # Consider only optimal solutions that end in New York.
            values = [
                new_york_costs[i] + opt_new_york[i - 1],
                new_york_costs[i] + opt_san_francisco[i - 1] + transition_cost,
            ]
            k = numpy.argmin(values)

            if k == NY_TO_NY_INDEX:
                current_city = NEW_YORK_LABEL
            elif k == SF_TO_NY_INDEX:
                current_city = SAN_FRANCISCO_LABEL

        elif current_city == SAN_FRANCISCO_LABEL:
            # Consider only optimal solutions that end in San Francisco.
            values = [
                san_francisco_costs[i] + opt_san_francisco[i - 1],
                san_francisco_costs[i] + opt_new_york[i - 1] + transition_cost
            ]
            k = numpy.argmin(values)

            if k == SF_TO_SF_INDEX:
                current_city = SAN_FRANCISCO_LABEL
            elif k == NY_TO_SF_INDEX:
                current_city = NEW_YORK_LABEL
        i -= 1
        solution.appendleft({CITY_LABEL: current_city, WEEK_LABEL: i + 1})
    return list(solution)
