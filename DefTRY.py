def FuncNameGoesHere():
    size = int(input())
    if 0 < size < 30:
        ct1 = int(1)
        ct2 = int(1)
        while ct1 <= size:
            while ct2 <= size:
                print(ct1 * ct2, " ", end='')
                ct2 = ct2 + 1
            ct1 = ct1 + 1
            ct2 = 1
            print(" ")
    return 

def AnotherFuncNameHere(array1, array2):
    ct1 = int(0)
    ct2 = int(0)
    while ct1 < len(array2):
        while ct2 < len(array1):
            if array2[ct1] == array1[ct2]:
                break
            ct2 = ct2 + 1
        if ct2 == len(array1):
                array1.append(array2[ct1])
        ct1 = ct1 + 1
        ct2 = 0
    print(array1)
    return

## FuncNameGoesHere()
AnotherFuncNameHere(["apple", "banana", "cherry"], ["happle", "hbanana", "hcherry"])

