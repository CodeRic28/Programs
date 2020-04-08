
def brac(exp): #(3*4/9*12*(5-10)/2000)*99*2+500
    while "(" in exp:

        c_brac = o_pos = exp.index(")")
        while exp[o_pos] != "(":
            o_pos -= 1
        o_brac = o_pos
        brac_exp = exp[o_brac+1 : c_brac]
        print('brac_exp',brac_exp)
        if '*-' in brac_exp or '/-' in brac_exp:
            val = stmin(brac_exp)
            exp = exp[:o_brac] + str(val) + exp[c_brac + 1:]
        else:
            exp = exp[:o_brac] + str(evaluate(brac_exp)) + exp[c_brac + 1:]
        #     if '*-' in exp or '/-' in exp:
        #         val = stmin(exp)
        #         exp = exp[:o_brac] + str(val) + exp[c_brac + 1:]
        # # stmin(brac_exp)
        # exp = exp[:o_brac] + str(evaluate(brac_exp)) + exp[c_brac + 1:]
        # stmin(exp)
    return evaluate(exp)

def lft(exp, pos):
    i = pos-1
    while exp[i].isnumeric() is True or exp[i] == '.':
        i=i-1
        if i<0:
            break
    return exp[i+1:pos]

def rgt(exp, pos):
    i = pos+1
    while exp[i].isnumeric() is True or exp[i] == '.':
        i=i+1
        if i > len(exp):
            i = len(exp)
            break
    return exp[pos+1:i]

def stmin(exp):
    if '*-' in exp:# or '/-' in exp or '+-' in exp or '--' in exp:
        star_pos = exp.find('*-')
        min_pos = star_pos + 1
        left = exp[:min_pos]
        right = exp[min_pos+1:]

        i = star_pos - 1
        while exp[i].isnumeric() is True or exp[i] == '.' or exp[i] == '*' or exp[i] == '/':
            i=i-1
            if exp[i] == '+' or exp[i] == '-':
                break
            elif i<0: break
        sign = i
        if exp[sign] == '+':
            exp = exp[:sign] + str('-') + exp[sign+1:min_pos] + exp[min_pos+1:]
        elif exp[sign] == '-':
            exp = exp[:sign] + str('+') + exp[sign+1:min_pos] + exp[min_pos+1:]
            if exp[0] == '+':
                exp = exp[1:]
        else:
            exp = exp[min_pos] + left + right

    elif '/-' in exp:
        star_pos = exp.find('/-')
        min_pos = star_pos + 1
        left = exp[:min_pos]
        right = exp[min_pos + 1:]

        i = star_pos - 1
        while exp[i].isnumeric() is True or exp[i] == '.' or exp[i] == '*' or exp[i] == '/':
            i = i - 1
            if exp[i] == '+' or exp[i] == '-':
                break
            elif i < 0:
                break
        sign = i
        if exp[sign] == '+':
            exp = exp[:sign] + str('-') + exp[sign + 1:min_pos] + exp[min_pos + 1:] - 3 * 4 / 9 * 12 * 5.0 / 2000
        elif exp[sign] == '-':
            exp = exp[:sign] + str('+') + exp[sign + 1:min_pos] + exp[min_pos + 1:]
            if exp[0] == '+':
                exp = exp[1:]
        else:
            exp = exp[min_pos] + left + right
    elif '^-' in exp:
        star_pos = exp.find('^-')
        min_pos = star_pos + 1
        left = exp[:min_pos]
        right = exp[min_pos+1:]

        l = lft(exp, star_pos)
        r = rgt(exp, star_pos)
        exp = exp[:star_pos-len(l)] + str('1/') + l + str('^') + r + exp[star_pos+len(r)+1:]

    print('exp', exp)
    return brac(exp)

def evaluate(exp):
    if '*-' in exp or '/-' in exp:
        exp = stmin(exp)
        if type(exp) is float:
            exp = str(exp)
    if "+" in exp:
        pos_op = exp.find("+")
        left = exp.split("+")[0]
        right = exp[pos_op + 1:]
        return evaluate(left) + evaluate(right)
    elif "-" in exp:
        pos_op = exp.find("-")
        left = exp.split("-")[0]
        if left == '':
            left = '0'
        if left[0] == "-":
            left = '0-'
        right = exp[pos_op + 1:]
        return evaluate(left) - evaluate(right)

    elif "*" in exp:
        pos_op = exp.find("*")
        left = exp.split("*")[0]
        right = exp[pos_op + 1:]
        return evaluate(left) * evaluate(right)
    elif "/" in exp:
        pos_op = exp.find("/")
        left = exp.split("/")[0]
        right = exp[pos_op + 1:]
        return evaluate(left) / evaluate(right)
    elif "^" in exp:
        pos_op = exp.find("^")
        left = exp.split("^")[0]
        right = exp[pos_op + 1:]
        return evaluate(left) ** evaluate(right)

    else:
        # Base Case
        #print("Execution completed")
        return float(exp)


inp = input("Enter an expression: ")
if "(" in inp:
    print(brac(inp))
else:
    print(evaluate(inp))
