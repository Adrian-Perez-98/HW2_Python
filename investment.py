def calculate_apr(principal, interest_rate, years):
    """This function calculates the value of an investment after x amount of years"""
    total = 0
    for i in range(1, years):
        total += principal(years + interest_rate)


if __name__ == '__main__':
    print(calculate_apr.__doc__)
    print(calculate_apr(500, .03, 65))
