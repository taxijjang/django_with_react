def mul(a,b):
    return a,b

def sum(a,b):
    return f"{a} + {b} = {a+b}"

a = 1
b = 1

print(sum(a,b))

@mul(a,b)
def deco(a,b):
    return f"{a} {b}"

print(deco(a,b))