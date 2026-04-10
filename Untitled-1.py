def tribonacci(signature, n):
    times = 3
    number = 0
    if n == 0: return []
    if n == 1: return [signature[0]]
    if n == 2: return [signature[0], signature[1]]      
    while times < n:
        signature.append(signature[number] + signature[number + 1] + signature[number + 2])
        times += 1
        number += 1
    return signature

print(tribonacci([300, 200, 100], 0))