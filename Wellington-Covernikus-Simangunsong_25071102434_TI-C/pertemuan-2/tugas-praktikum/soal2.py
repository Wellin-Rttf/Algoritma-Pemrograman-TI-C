def bilangan_prima(n):
    prima = []
    for x in range(2, n+1):
        bilanganPrima = True
        for y in range(2, int(x**0.5) + 1):
            if x % y == 0:
                bilanganPrima = False
                break
        if bilanganPrima:
            prima.append(x)
    return prima

print("Bilangan prima sampai 50:", bilangan_prima(50))