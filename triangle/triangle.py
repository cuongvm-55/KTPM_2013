def testInputRange(a):
    if (a < 0) or (a > 2**32-1) :
        return False
    return True

def is_number(s):
    try:
        float(s)
    except ValueError:
        return False
    return True

def testInputType(a):
    if type(a) not in [float,int,long] :
        return False
    return True

def KiemTraTamGiac(a, b, c) :
    if testInputType(a) == False or testInputType(b) == False or testInputType(c) == False :
        return "Input Type Error"
    
    if testInputRange(a) == False or testInputRange(b) == False or testInputRange(c) == False :
        return "Input Range Error"

    if (a == b) and (b == c) :
        return "Deu"
    elif (a == b) or (b == c) or (c ==a ) :
        if (a*a + b*b - c*c < 0.000001) or (b*b + c*c - a*a < 0.000001) or (a*a + c*c - b*b < 0.000001):
            return "Vuong Can"
        else :
            return "Can"
    else :
        if (a*a + b*b == c*c) or (b*b + c*c == a*a) or (a*a + c*c == b*b):
            return "Vuong"
        else :
            return "Thuong"

