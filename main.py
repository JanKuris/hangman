import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


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

    confirm = input("Are you sure you want to use this letter? y/n ").lower()
    if confirm == "y":
        continue
    elif confirm == "n":
        user_input
    else:
        print(f"Invalid input. Please put 'y' or 'n' {confirm}")

 
        
        for position in range(word_lenght):
          letter = chosen_word[position]
        if letter == user_input:
            display[position] = letter
    

        
    # if not display == display:
    #     break
    print(display)
    
    

