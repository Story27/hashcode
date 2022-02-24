file = open("initial.txt")
lines = file.readlines()
print(lines)


a = open("input.txt","a+")
b = a.readlines()
c =len(b)
for n in (0,c):
    b[n] = b[n].split("/n")
print(b)
