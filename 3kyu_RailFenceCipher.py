def encode_rail_fence_cipher(string, n):
    result = ["" for i in range(n)]
    idx, lane, direction = 0, 0, 1
    while idx < len(string):
        result[lane] += string[idx]
        idx += 1
        lane += direction
        if lane == n-1 : direction = -1
        elif lane == 0 : direction = 1
    return "".join(result)
            
def decode_rail_fence_cipher(string, n):
    cycle = 2 * (n-1)
    leng = len(string)
    result = []
    size = 0
    for i in range(1,n+1):
        if i == 1 or i == n : rail = (leng + cycle - i)// cycle
        else : rail = ((leng + i - 2)// cycle) + ((leng + cycle - i)// cycle)
        result.append(string[size:size+rail])
        size += rail
    
    lane, direction, idx = 0, 1, 0
    output = ""
    while len(output) < len(string):
        output += result[lane][0]
        result[lane] = result[lane][1:]
        lane += direction
        if lane == n-1 : direction = -1
        elif lane == 0 : direction = 1
    return output
    
