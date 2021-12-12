def penjumlahanAngka(searchDis, target):
    toBeReturned = []
    ct1 = int(0)
    ct2 = int(0)
    while ct1 < len(searchDis):
        while ct2 < len(searchDis):
            if ct1 != ct2 and searchDis[ct1] + searchDis[ct2] == target:
                toBeReturned.append(ct1)
                toBeReturned.append(ct2)
                return toBeReturned
            ct2 = ct2 + 1
        ct1 = ct1 + 1
        ct2 = ct1 + 1
    return toBeReturned

print(penjumlahanAngka([1, 2, 3, 4, 6], 6))
print(penjumlahanAngka([2, 5, 9, 11], 11))

x = int(input())



