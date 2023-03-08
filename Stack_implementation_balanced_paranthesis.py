l=[]
def popfunc():
    if len(l)==0:
        return None
    else:
        p=l[len(l)-1]
        del l[len(l)-1]
        return p
    
def pushfunc(pu):
    l.append(pu)
    
def isemp():
    if len(l)==0:
        return True
    else:
        return False

def ismatched(expr):
    lefty='([{'
    righty=')]}'
    for c in expr:
        if c in lefty:
            pushfunc(c)
        elif c in righty:
            if isemp():
                return False
            if righty.index(c) != lefty.index(popfunc()):
                return False
    return isemp()

expr= input('Enter the expression: ')
op=ismatched(expr)
if op==True:
    print('Balanced braces')
else:
    print('Braces not balanced')
