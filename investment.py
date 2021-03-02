def calculate_apr(principal=0, interest_rate=0, years=0):
    """This function calculates the value of an investment after x amount of years"""
    return float(principal*(1+(interest_rate*years)))


if __name__ == '__main__':
    print(calculate_apr.__doc__)
    print(calculate_apr(500, .03, 65))
