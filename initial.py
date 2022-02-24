file = open("initial.txt")
lines = file.readlines()
print(lines)


a = open("input.txt","a+")
b = a.readlines()
c =len(b)
for n in (0,c):
    b[n] = b[n].split("/n")
print(b)



anna = {"C++" : "2"}
bob = {"HTML": "5","CSS" : "5"}
maria = {"Python" : "3"}
logging = ("5","10","5","1")
req1 = {"C++" : "3"}
WebServer = ("7","10","7","2")
req2 = {"HTML" : "3","C++" : "2"}
WebChat = ("10","20","20","2")
req3 = {"Python" : "3","HTML" : "3"}
