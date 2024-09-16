#Addition

def do_addition(a:int,b:int):
    return a+b

def do_subtraction(a:int,b:int):
    return a-b

def do_division(a:int, b:int):
    try:
        return a/b
    except ZeroDivisionError as e:
        return "Can not divided by Zero"