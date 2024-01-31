import random


word_list = ["dog", "pencil", "baboon"]
chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)
letter_list = list(chosen_word)
print(chosen_word)

display = []
for _ in range(word_lenght):
    display += "_"
print(display)


while display != letter_list:
    user_input = input(f"Guess a letter:\n").lower()
        
    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == user_input:
            display[position] = letter
 
    if not display == display:
        break
    print(display)
    print("win")

  

       