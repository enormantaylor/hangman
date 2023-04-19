import random

word_list = ["tokyo", "london", "paris", "berlin", "newyork"]

random_word = random.choice(word_list)


print(random_word)
length = len(random_word)

display = []


for x in range(length):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("guess a letter: ").lower()
    for pos in range(length):
        letter = random_word[pos]
        if guess == letter:
            display[pos] = letter

    print(display)


    if "_" not in display:
        end_of_game = True
        print("ayyy")