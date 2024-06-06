import math

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def activate_function():
    x = input("Input x = ")

    if not is_number(x):
        print("x must be number")
        return
    
    x = float(x)

    sigmoid = 1 / (1 + math.exp(-x))
    relu = max(0, x)
    elu = x if x > 0 else 0.01 * (math.exp(x) - 1)

    choose_activate_function = input("Input activation function (sigmoid | relu | elu): ")

    if choose_activate_function not in ["sigmoid", "relu", "elu"]:
        print(f"{choose_activate_function} is not supported")
        return
    
    if choose_activate_function == "sigmoid":
        print(f"sigmoid: f({x}) = {sigmoid}")
    elif choose_activate_function == "relu":
        print(f"relu: f({x}) = {relu}")
    elif choose_activate_function == "elu":
        print(f"elu: f({x}) = {elu}")

activate_function()