# https://leetcode.com/problems/average-waiting-time/description/?envType=daily-question&envId=2024-07-09

def averageWaitingTime(customers: List[List[int]]) -> float:
    n = len(customers)
    currentTime = 0
    totalTime = 0
    for i in range(n):
        st = customers[i][0]
        work = customers[i][1]
        # If we can do work immediatly no special case
        if currentTime <= st:
            totalTime += work
            currentTime = st + work
        # Otherwise we need to account in the difference between the current time and given start Time
        else:
            totalTime += (currentTime - st + work)
            currentTime += work
    return totalTime / n
