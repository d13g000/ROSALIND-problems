def total_rabbit_pairs(n, k):  # n = number of months, k = number of rabbit
    """This code determines the number of pairs of offspring pairs produced
    after n months, where each mature rabbit produces a litter of k pairs
    (considering the reproductive age of rabbits is 2 months)."""
    previous, current = 0, 1  # Initial cases where; month 0 = 0 rabbit pairs
    # and, month 1: 1 rabbit pair

    for _ in range(2, n + 1):  # Run through months 2 - n (where n is included)
        previous, current = current, current + previous * k  # Update values
        # using the recurrence relation

    return current

n, k = 5, 3 # 5 months, 3 rabbit pairs produced each mating round

print(total_rabbit_pairs(n, k))