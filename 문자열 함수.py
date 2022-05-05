string="hello,world"
print(string.count("h"))
print(string.index("w"))
print(string.index("w"))
print(",".join(string))

print(string.replace("world","subin"))
print(string.replace("world",""))

tmp=string.split(',')
print(tmp)
print(",".join(tmp))
print(string[:string.index(",")])

l = [1, 2, 3, 4, 5]
print(l.index(3))
print(l[2:4])
