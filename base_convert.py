# int int -> str
# returns a string representing num in the base b
def convert(num, b):
    # finds the quotient of the num and the base
    quotient = num//b

    # stops if quotient is 0
    if quotient == 0:
        return num

    # assigns remainder
    else:
        remainder = num%b

        # assigns the letter symbols if the remainder >= 10
        if remainder >= 10:
            symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            remainder = symbols[remainder-10]
        return str(convert(quotient, b)) + str(remainder)
