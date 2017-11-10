# Prvočísla
N = int(input("Do kolika? "))
prvocisla = []

# Procházení čísel 2 až N
for n in range(2, N+1):
    for p in prvocisla:
        if n % p == 0:
            break
    else:
        prvocisla.append(n)

# Vytisknutí nalezených prvočísel
print(prvocisla)
