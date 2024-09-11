def show_rest():
    #get value
    divisor = int(input('Enter divisor'))
    dividend = int(input('Enter dividend'))
    # calculate
    rest = divisor % dividend
    return rest

def show_increase():
    # get value
    increase = 0.1
    salary = 200000
    # calculate
    salary_with_increase = salary * (1 + increase)
    # show message
    return salary_with_increase

def show_discount():
    # get value 
    discount = 0.25
    salary = 1000000
    # calculate
    salary_discount = salary * (1 - discount)
    # show
    return salary_discount