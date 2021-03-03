def calculate_apr(principal, interest_rate, years):
    """This function calculates the value of an investment after x amount of years"""
    if principal < 0 and interest_rate < 0 and years < 0:
        return False
    for i in range(0, years):
        total = float(principal * (years + interest_rate))
    return total


if __name__ == '__main__':
    print(calculate_apr.__doc__)
    print(calculate_apr(500, .03, 65))
