#https://www.hackerrank.com/challenges/counting-valleys/problem
def countingValleys(steps, path):
    mountain = valley = 0
    for word in path:
        mountain += 1 if word == 'U' else -1
        valley += 1 if mountain == 0 and word == 'U' else 0
    return valley
    
