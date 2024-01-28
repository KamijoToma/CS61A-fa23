def nearest_two(x):
    """Return the power of two that is nearest to x.

    >>> nearest_two(8)    # 2 * 2 * 2 is 8
    8.0
    >>> nearest_two(11.5) # 11.5 is closer to 8 than 16
    8.0
    >>> nearest_two(14)   # 14 is closer to 16 than 8
    16.0
    >>> nearest_two(2015)
    2048.0
    >>> nearest_two(.1)
    0.125
    >>> nearest_two(0.75) # Tie between 1/2 and 1
    1.0
    >>> nearest_two(1.5)  # Tie between 1 and 2
    2.0

    """
    power_of_two = 1.0
    next = 1/2
    "*** YOUR CODE HERE ***"
    square = lambda x: x*x
    while min(power_of_two, power_of_two*next, x) == x or \
    max(power_of_two, power_of_two*next, x) == x:
        print(f"DEBUG: {power_of_two}, {power_of_two*next}, {x}")
        if min(power_of_two, power_of_two*next) > x and next == 2:
            next = 1/2
            continue
        elif min(power_of_two, power_of_two*next) == x:
            return min(power_of_two, power_of_two*next)
        elif min(power_of_two, power_of_two*next) < x and next == 1/2:
            next = 2
            continue
        power_of_two = power_of_two * next
    if abs(power_of_two - x) < abs(power_of_two*next - x):
        return power_of_two
    elif abs(power_of_two - x) > abs(power_of_two*next - x):
        return power_of_two*next
    else:
        return max(power_of_two, power_of_two*next)

if __name__ == '__main__':
    print(nearest_two(.75))