import random


word_list = ["dog", "pencil"]
chosen_word = random.choice(word_list)
# chosen_word = list(random_word)
word_lenght = len(chosen_word)

display = []
for _ in range(word_lenght):
    display += "_"
print(display)

while chosen_word != display:
    user_input = input(f"Guess a letter:\n").lower()
        
    for position in range(word_lenght) :
        letter = chosen_word[position]
        if letter == user_input:
            display[position] = letter
    
        

    print(display)
