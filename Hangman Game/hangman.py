import random
import words

word = words.words
word = random.choice(word)

def hangman_visual(mistake):
    if mistake >= 1:
        print("   O ")
    if mistake >= 2:
        print("  /|\ ")
    if mistake >= 3:
        print(" / | \ ")
    if mistake >= 4:
        print("   |  ")
    if mistake >= 5:
        print(" /   \ ")



def hangman_game():
    want_guess = list(map(str, word))
    change_guess = list(map(str,"_" * len(word)))
    used_words=[]
    mistake = 0
    
    print("Hello, Welcome hangman game :)")
    print("You have 5 try for win")
    win =0
    print(change_guess)
    while True:
        letter = input("Please enter a letter : ")
        if letter=="":
            print("Please Enter a letter, don't skip !!")
            
        elif letter in used_words:
            print("You Already Use This Letter")
            print(change_guess)  
        else:    
            for a in range(len(word)):

                if letter == word[a]:
                    change_guess[a] = letter
                    used_words.append(letter)
                    win +=1
            print(change_guess)         
            if letter not in word:
                mistake +=1
                hangman_visual(mistake)
                used_words.append(letter)

            if mistake == 5:
                print("Answer was : {}".format(word))
                print("Your Man are dead :(")
                print("Try Again")
                
                break
            if win == len(word):
                print("Great, You Win :)")
                break
    
   

hangman_game()