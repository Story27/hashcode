file = open("initial.txt")
lines = file.readlines()
print(lines)


a = open("input.txt","r")
b = a.readlines()
c =len(b)
for n in (0,c):
    n=0
    b[n] = b[n].split("/n")
print(b)
