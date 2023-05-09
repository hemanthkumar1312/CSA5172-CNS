n = "abcdefghijklmnopqrstuvwxyz"
li, mi = [], []
z, x = " "," "
key = int(input("Enter the key value:"))
s = str(input("Enter the plain text:"))
print("!encryption!")
for i in range(len(s)):
    k = n.find(s[i])
    k = k + key
    m = k % 26
    li.append(m)
for i in range(len(li)):
    l = li[i]
    z = z + n[l]
print(z)
print("!decryption!")
for i in range(len(z)):
    o = n.find(z[i])
    o = o - key
    h = o % 26
    mi.append(h)
for i in range(1,len(li)+1):
    p = mi[i]
    x = x + n[p]
print(x)
