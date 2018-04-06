print("The number of iterations before the function M(c) = z^2 + c reaches the value of 2 (and thereafter diverges) approaches the digits of Pi for certain values of c\n")

def Mndlbrt(z, c): #The Mandelbrot function
    n = z**2 + c
    return n

def N(c):
    z = 0
    i = 0
    while z < 2:
        z = Mndlbrt(z, c)
        i += 1
    print("Number of iterations: " + str(i)) #prints the number of iterations until z > 2 (assuming c is outside the M set)

def iterating_c():
    extra = 1
    while True:
        c = 0.25 + extra
        N(c)
        extra = extra / 100 #not sure why c must be 100x smaller each time

iterating_c()
