def safe_divide(numerator, denominator):
    try:

        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        return "The result of the division is " + str(result)

    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except ValueError:
        return "Error: Please enter numeric values only."
