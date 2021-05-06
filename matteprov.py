import random

print("Matteprovet börjar här.")
score = 0

while True:
    n = random.randint(0, 10)
    m = random.randint(0,10)

    print("Vad är", n, "plus", m)
    svar = int(input())
    if svar == -1:
        break
    if svar == n + m:
        print("Rätt!")
        score += 1  # score = score + 1
    else:
        print("Fel!")
        print("Rätt svar är:", n + m)
    print("Dina poäng:", score)
print("Matteprovet slutar här.")
