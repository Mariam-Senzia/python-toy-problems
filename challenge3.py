# integer n returns string of length N containing many different lower case letters....occurs equal number of times

def solution(N):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ""

    if N % 2 == 0 or N % 3 == 0:
        for i in range(N):
            result += alphabet[i % 26]
    else:
        for i in range(N):
            result += alphabet[(i % 25) + 1]

    return result

print(solution(3))   
print(solution(5))   
print(solution(30))  