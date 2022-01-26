import random
words = ["apple", "pineapple", "hero", "world", "photosynthesis"]
n = 0
chance = 5
j = 0
p = 0
Trial = []
word = random.choice(words)
for i in range(0, len(word)):
    Trial.append("_")                  # khali list ma paxi trial[n]= garera assign garna mildaina
while chance != 0:
    guess = input("Guess ")
    for letter in word:
        if guess == letter:
            Trial[n] = guess
            j = 1
        n = n+1
    n = 0
    if j == 0:
        chance = chance-1
    j = 0
    print(Trial)
    for check in Trial:
        if check == "_":
            p = 1
    if p == 0:
        print("Wiiin")
        quit()
    p = 0
    print(f"{chance} chances remaining")
print("Looose")
