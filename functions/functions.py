def format_number(number):
    try:
        number = abs(float(number))
    except ValueError:
        print(f"You have entered invalid number. Entered value : {number}")
        return 0
    else:
        return number