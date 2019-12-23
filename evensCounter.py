import util
EVENSLIST = []
for x in range(1,16):
    EVENSLIST.append(util.load("../../../Desktop/evens/evens" + str(x) + ".dat"))
for x in range(1,16):
    print("number of evens up to " + str(x) + "x" + str(x) + ":")
    tot = 0
    for y in range(0, x):
        for z in EVENSLIST[y]:
            if z[0] <= x:
                tot+=1
    print(tot)
    
