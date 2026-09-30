def product(term1, term2):
    return term1*term2

if __name__ == "__main__":

    a: int = 4
    b: int = 5
    r: int = 6
    s: int = 7

    prod1: int = product(a,b)
    prod2: int = product(r,s)

    resultado: int = prod1 + prod2

    print(resultado)
