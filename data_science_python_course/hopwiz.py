for n in range(1, 100):
    result = "Hop-Viz" if not n % 15 else "hop" if not n % 3 else "Viz" if not n % 7 else str(n)
    print(result)
