d={100:"Manya",200:"Mahek",300:"Raj",400:"Ronik"}

print(d)
d1=d.copy()
print(d1)

print(d.get(100))
print([300])
print(d[200])
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(200))
print(d)

d2={500:"Aayush",600:"Aryan",700:"Yash",800:"Kush"}
d.update(d2)
print(d)
d[900]="Deep"
print(d)

for i in d:
    print(i)

for i in d:
    print(i," : ",d[i])
