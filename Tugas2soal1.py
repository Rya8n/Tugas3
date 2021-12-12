def angkaMunculSekali(searchDis):
    toBeReturned = []
    ct1 = int(0)
    ct2 = int(0)
    while ct1 < len(searchDis):
        while ct2 < len(searchDis):
            if ct1 != ct2 and searchDis[ct1] == searchDis[ct2]:
                break
            ct2 = ct2 + 1
        if ct2 == len(searchDis) and searchDis[ct1] != searchDis[ct2 -1]:
            toBeReturned.append(searchDis[ct1])
        if ct2 == len(searchDis) and ct1 == ct2 - 1:
            toBeReturned.append(searchDis[ct1])
        ct1 = ct1 + 1
        ct2 = 0
    return toBeReturned


print(angkaMunculSekali("76523752"))
print(angkaMunculSekali("1122"))
print(angkaMunculSekali("1234123"))

x = int(input())



