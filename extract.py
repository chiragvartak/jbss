import sys

f = open(".problem-instances.txt", 'r')

line = f.readline()
while line:
    stripped = "".join(line.split())
    if stripped != "" and stripped[0] != "#":
        bs = eval(line)
        user = eval(f.readline())
        print(len(user))
        print(len(bs))
        u = ['u' + str(x) for x in user]
        b = ['b' + str(x) for x in bs]
        entities = u + b
        entities.sort(key=lambda x: int(x[1:]))
        for i in entities:
            print(i)
        print()
    line = f.readline()

f.close()
