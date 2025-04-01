def bin_search(ordered_array, search_value):
    print(f"Ordered-Array to search: {ordered_array}")
    # set lower_bound
    lb = 0
    # set upper bound
    ub = len(ordered_array) - 1

    print(f"start lower-bound: {lb}")
    print(f"start upper-bound:{ub}")
    print("*" * 20)
    # number of checks
    numChecks = 1
    while lb <= ub:
        # calculate midpoint
        midPoint = int((lb + ub) / 2)
        # midpoint
        print(f"midpoint index- {midPoint}")
        # read midpoint value
        midPointValue = ordered_array[midPoint]
        print(f"midpoint value - {midPointValue}")

        # check if search_value is the midpoint
        if search_value == midPointValue:
            print(f"{search_value} found at index {midPoint}")
            print(f"number of checks - {numChecks}")
            return 1
        elif search_value < midPointValue:
            # update upper bound
            ub = midPoint - 1
            print("*" * 20)
            print("updating upper-bound")
            print(f"lower-bound: {lb}")
            print(f"updated upper-bound:{ub}")
            print("*" * 20)

        elif search_value > midPointValue:
            # update lower bound
            lb = midPoint + 1
            print("*" * 20)
            print(f"updated lower-bound: {lb}")
            print(f"upper-bound:{ub}")
            print("*" * 20)
        numChecks += 1

    print(f"number of checks - {numChecks}")
    print(f"{search_value} not found in {ordered_array}")
    return 0


bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
bin_search(list(range(1, 101)), 100)
