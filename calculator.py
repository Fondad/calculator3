def calculator(x,y,sign):
    # This is an unwanted but staged comment
    if sign == "+":
        return x + y
    elif sign == "-":
        return x - y
    elif sign == "*":
        return x * y
    elif sign == "/":
        if y == 0:
            return None
        return x / y
    return None
