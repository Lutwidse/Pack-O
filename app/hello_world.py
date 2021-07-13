import random, time

print("rot13")
a, b, c, d, e, f = 2, 4, 6, 8, 10, 12
abcdef = (a + b - c * d / e) ** f
rand = abcdef + random.randint(1, 100) * time.time() / random.randint(1, 10) % time.time()
print(rand)