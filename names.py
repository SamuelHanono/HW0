import string

#------------------------------------------------------------------------------
# In this section, define a function that returns your name

def james():
    def f(x): return (24*x**4 - x**3 + 5*x**2 - 8*x + 9) % 29
    return ''.join(string.ascii_lowercase[f(n)] for n in range(5)).capitalize()

def mario():
    start: int = 100
    jumps: list[int] = [9, -3, 14, 5, 11, -1, 11, 0, 1, 15, 2, 11, 14, 2, 17, 10]
    return ''.join(chr(start + j) for j in jumps).capitalize()

#------------------------------------------------------------------------------


# Add your function to the list here
NAME_FUNCTIONS = [james, mario]


# Don't edit this
for f in NAME_FUNCTIONS:
    print(f())