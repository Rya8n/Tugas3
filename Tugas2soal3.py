def totalKemunculan(searchDis):
    itemList = []
    appearanceCount = []
    ct1 = int(0)
    ct2 = int(0)
    itemList.append(searchDis[0])
    while ct1 < len(searchDis):
        while ct2 < len(itemList):
            if searchDis[ct1] == itemList[ct2]:
                break
            ct2 = ct2 + 1
        if ct2 == len(itemList) and searchDis[ct1] != itemList[ct2 - 1]:
            itemList.append(searchDis[ct1])
        ct2 = 0
        ct1 = ct1 + 1
    ct1 = 0
    ct2 = 0
    ctct = 0
    while ct1 < len(itemList):
        while ct2 < len(searchDis):
            if itemList[ct1] == searchDis[ct2]:
                ctct = ctct + 1
            ct2 = ct2 + 1
        appearanceCount.append(ctct)
        ctct = 0
        ct2 = 0
        ct1 = ct1 + 1
    ct1 = 0
    while ct1 < len(itemList):
        print(itemList[ct1] + ":", appearanceCount[ct1])
        ct1 = ct1 + 1
    return

totalKemunculan(["js","js","golang","ruby","ruby","js","js"])
totalKemunculan(["danu", "danu", "alif", "indra", "indra", "kurniadi", "indra"])
x = int(input())



