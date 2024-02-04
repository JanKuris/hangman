import random
from replit import clear
from hangman_art_caption import caption
from hangman_art import stages

WORD_LIST_FILE = "hangman_words.txt" 

lives = 6
end_of_game = False
inFile = open(WORD_LIST_FILE, 'r')
line = inFile.readline()
word_list = line.split()
chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)
display = []


for _ in range(word_lenght):
    display += "_"

while not end_of_game:
    
    user_input = input(f"Guess a letter:\n").lower()  

    clear()

    # confirm = input("Are you sure you want to use this letter? y/n ").lower()
    # for i in confirm:
    #   if confirm == "y":
    #       user_input
    #   elif confirm == "n":
    #       continue
    #   else:
    #       print(f"Invalid input. Please put 'y' or 'n' {confirm}")

 
        
    for position in range(word_lenght):
      letter = chosen_word[position]
      if letter == user_input:
        display[position] = letter

    
    if user_input not in chosen_word:
        lives -= 1
        if lives == 0:
            print(f"You guessed {user_input}, that's not in the word. You lose the life")
            print(stages[lives])
            break
            

    print(f"{' '.join(display)}")

    if  "_" not in display:
        # end_of_game == True
        print("win")
        break 
        

    print(stages[lives])  

      
    

        
    
            
    
    

