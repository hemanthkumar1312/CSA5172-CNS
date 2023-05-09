n = "abcdefghijklmnopqrstuvwxyz"
s = str(input("Enter the plain text:"))
p = "lzmynxowpvqurtsjaibhcgdfde"
li = []
a, b = " ", " "
for i in range(len(s)):
    k = n.find(s[i])
    li.append(k)
for j in range(len(s)):
    a = a + p[li[j]]
for j in range(len(s)):
    b = b + n[li[j]]
print("!encryption!")
print(a)
print("!decryption!")
print(b) 
