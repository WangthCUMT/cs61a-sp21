def gcd(a,b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif max(a,b) % min(a,b) == 0:
        return min(a, b)
    else:
        return gcd(min(a,b) , max(a,b) % min(a,b))

def square(x):
    return x*x

def pow1(base,exp):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        return square(pow1(base,exp/2))
    else:
        return base * pow1(base,exp-1)

def cube(x):
    return x ** 3

def repeatly_cube(n,x):
    if n == 0:
        return x
    else:
        return repeatly_cube(n-1, cube(x))
