# https://leetcode.com/problems/crawler-log-folder/?envType=daily-question&envId=2024-07-10
def minOperations(self, logs: List[str]) -> int:
    dist = 0
    for i in range(len(logs)):
        move = logs[i]
        if move == '../':
            dist = dist - 1 if dist > 0 else 0
        elif move == './':
            continue
        else:
            dist = dist + 1
    return dist
