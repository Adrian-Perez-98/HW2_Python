def calculate_apr(principal=0, interest_rate=0, years=0):
    """This function calculates the value of an investment after x amount of years"""
    return round(principal*(1+(interest_rate*years)), 2)


if __name__ == '__main__':
    print(calculate_apr.__doc__)
    print(calculate_apr(10000, .03875, 5))
