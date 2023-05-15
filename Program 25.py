import math


n = 200
e = 23


c = [346, 189, 469, 294, 207, 444]


for i in range(len(c)):
    gcd = math.gcd(c[i], n)
    if gcd != 1:
        p = gcd
        break


q = n // p


phi = (p-1) * (q-1)
d = pow(e, -1, phi)


m = []
for i in range(len(c)):
    m.append(pow(c[i], d, n))


print("Decrypted message: ", end="")
for i in range(len(m)):
    print(chr(m[i]), end="")
print()
