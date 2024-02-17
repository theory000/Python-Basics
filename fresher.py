scores = []
for i in range(3):
    score = int(input("Score: "))
    scores.append(score)

print(scores)

average = sum(scores) / len(scores)
print(f"Average: {average}")