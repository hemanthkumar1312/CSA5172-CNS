key = str(input("Enter key content:"))
plain = str(input("Enter plain text:"))
y, z= " "," "
n = "abcdefghijklmnopqrstuvwxyz"
print("!encryption!")
li1, li2, li3= [], [], []
for i in range(len(key)):
    m = n.find(key[i])
    li1.append(m)
li4 = []
for j in range(len(plain)):
    k = n.find(plain[j])
    li4.append(k)
li2 += li1
for i in range(len(plain)):
    li2.append(li2[i])
for j in range(len(plain)):
    li3.append(li2[j])
#li4 contain plain text alphabet value
#li3 contain key content alphabet value
li5 = []
for i in range(len(plain)):
    l = li4[i]+li3[i]
    li5.append(l)
#li5 contains key+pt
li6 = []
for i in range(len(li5)):
    o = li5[i]%26
    li6.append(o)
    y = y + n[o]
print(y)
li7 = []
print("!decryption!")
print(plain)
"""for i in range(len(plain)):
    b = n.find(y[i])
    print(b)
    li7.append(b-li3[i])
print(li7)"""
    
