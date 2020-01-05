import math

def find_expression(text):
    for i in range(len(text)-1,-1,-1):
        if text[i] == "+" or text[i] == "-" : return i

def combi(n, r) :
    return (math.factorial(n) // ( math.factorial(n-r) * math.factorial(r) ))

def expand(expr):
    idx = find_expression(expr)
    a_const = expr[expr.find("(")+1 : idx-1]
    if a_const == "" : a_const = 1
    elif a_const == "-" : a_const = -1
    else : a_const = int(a_const)
    b_const = int(expr[idx : expr.find(")")])
    variable = expr[idx-1]
    n_const = int(expr[expr.find("^")+1 :])
    print(a_const, variable, b_const, n_const)
    result = ""
    if n_const == 0 : result = "1"
    elif b_const == 0 : result = str(a_const**n_const) + variable + "^" + str(n_const)
    else :
        for i in range(n_const + 1):
            x = combi(n_const,i)*(a_const**(n_const-i))*(b_const**i)
            if i != 0 and x > 0 : result += "+"
            if x < 0 : result += "-"
            if i == n_const or (i != n_const and abs(x) > 1) : result += str(abs(x))
            if i != n_const :
                result += variable
                if i != n_const-1 : result += "^" + str(n_const-i)
            
    return result
