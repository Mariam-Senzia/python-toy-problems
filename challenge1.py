# N boxes, 0 - N-1 ,,,row
# Kth box A[K] bricks
# move, move brick to left r right

# min moves, end up with 10 bricks in every box

def solution(A):
    N = len(A)
    
    total_bricks = sum(A)
    
    if total_bricks % N != 0:
        return -1
    
    target_bricks = total_bricks / N
    
    
    moves = 0
    current_bricks = 0
    
    for i in range(N):
        diff = A[i] - target_bricks
        current_bricks += diff
        moves += abs(current_bricks)
    
    return int(moves)

print(solution([7, 15, 10, 8])) 
print(solution([[11, 10, 8, 12, 8, 10, 11]]))
print(solution([7, 14, 10]))   