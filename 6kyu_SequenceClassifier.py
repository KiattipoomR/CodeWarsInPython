def sequence_classifier(arr):
    code = {0,1,2,3,4,5}
    inp = set()
    if len(set(arr)) == len(arr) :
        inp = {2,4,5}
    for i in range(len(arr)-1) :
        if arr[i] != arr[i+1] :
            inp.add(5)
            if arr[i] > arr[i+1] :
                inp.add(1)
                inp.add(2)
            else :
                inp.add(3)
                inp.add(4)
    return list(code.difference(inp))[-1]
