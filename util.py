n = 11
x = [round(-4 + i * 0.4, 3) for i in range(11)]
y = [round((15 * i) / (i ** 4 + 4), 3) for i in x]
phi = [round(-1.9742 - 0.3714 * i, 3) for i in x]
phi2 = [round(-1.018 + 1.222 * i + 0.398 * i ** 2, 3) for i in x]
delta = [round((i - j) ** 2, 3) for i, j in zip(y, phi)]
delta2 = [round((i - j) ** 2, 3) for i, j in zip(y, phi2)]
sigma = round((sum(delta) / n) ** 0.5, 3)
sigma2 = round((sum(delta2) / n) ** 0.5, 3)
sx = round(sum(x), 3)
sxx = round(sum([i * i for i in x]), 3)
sxxx = round(sum([i ** 3 for i in x]), 3)
sxxxx = round(sum([i ** 4 for i in x]), 3)
sy = round(sum(y), 3)
sxy = round(sum([i * j for i, j in zip(x, y)]), 3)
sxxy = round(sum([i ** 2 * j for i, j in zip(x, y)]), 3)
print(*x)
print(*y)
print(*phi, sep="\t")
print(*delta, sep="\t")
print(sigma)
print(*phi2, sep="\t")
print(*delta2, sep="\t")
print(sigma2)
print(sx, sxx, sxxx, sxxxx, sy, sxy, sxxy)