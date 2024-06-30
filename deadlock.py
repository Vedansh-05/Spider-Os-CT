def find_deadlock(processes, allocation, request):
    n = len(processes)
    available = [sum(allocation[i]) for i in range(n)]
    
    # Step 1: Initialize flags and data structures
    work = available[:]
    finish = [False] * n
    deadlock_detected = False
    
    # Step 2: Find a process that can be finished
    while True:
        found = False
        for i in range(n):
            if not finish[i] and all(request[i][j] <= work[j] for j in range(n)):
                # Process i can finish
                finish[i] = True
                for j in range(n):
                    work[j] += allocation[i][j]
                found = True
        
        if not found:
            break
    
    # Step 3: Check for deadlock
    if not all(finish):
        deadlock_detected = True
    
    return deadlock_detected

# Example usage

processes = ['P0', 'P1', 'P2', 'P3']
allocation = [
    [0, 1, 0, 2],
    [1, 0, 3, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
request = [
    [0, 0, 1, 0],
    [2, 0, 0, 3],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
    
deadlock_detected = find_deadlock(processes, allocation, request)
    
if deadlock_detected:
    print("Deadlock detected! System is in a deadlock state.")
else:
    print("No deadlock detected. System is deadlock-free.")
