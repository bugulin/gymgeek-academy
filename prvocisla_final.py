# Prvočísla
N = int(input("Do kolika? "))
prvocisla = []

# Procházení čísel 2 až N
for n in range(2, N+1):
    i = True

    for p in prvocisla:
        if n % p == 0:
            i = False
            break

    if i:
        prvocisla.append(n)

# Vytisknutí nalezených prvočísel
for p in prvocisla:
    print("{:3}".format(p))
