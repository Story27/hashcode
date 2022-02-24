anna = {"C++" : "2"}
bob = {"HTML": "5","CSS" : "5"}
maria = {"Python" : "3"}
logging = ("5","10","5","1")
req1 = {"C++" : "3"}
WebServer = ("7","10","7","2")
req2 = {"HTML" : "3","C++" : "2"}
WebChat = ("10","20","20","2")
req3 = {"Python" : "3","HTML" : "3"}

a = req1.get("C++")
b = anna.get("C++")
c = bob.get("CSS")
d = bob.get("HTML")
e = maria.get("Python")
f = req2.get("C++")
g = req2.get("HTML")
h = req3.get("HTML")
i = req3.get("Python")
diction = {}
diction['3'] = 'three projects are planned'
diction['Logging'] = 'assignments for project Logging'
if a>b or a==b:
    diction['anna'] = 'Anna → first role'

diction['WebServer'] = 'assignments for project WebServer'
if (d>g or d==g) and (b>f or b==f):
    diction['Bob Anna'] = 'Bob → first role, Anna → second role'

diction['WebChat'] = 'assignments for project WebChat'
if (d>h or d==h) and (e>i or e==i):
    diction['Maria Bob'] = 'Maria → first role, Bob → second role'
print(diction)
