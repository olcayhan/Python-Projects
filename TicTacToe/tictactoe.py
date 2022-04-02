import random
import time



board = ["_","_","_","_","_","_","_","_","_"]



def Show_board():
    
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

def play_game():
        nchoosen.remove(number)
        board[number]="X"
        return Show_board()

      


def play_game_oppenet():
        print(" For Opponent")
        time.sleep(1)
        rand_number=random.choice(nchoosen)
        nchoosen.remove(rand_number)
        board[rand_number]="O"
        return Show_board()


    


print("Hello Welcome to tic tac toe game :)")
nchoosen = [0,1,2,3,4,5,6,7,8]
while True:
    print("Enter the number within the range(0-8)")
    number=int(input("Plase choose the number to play : "))
    
    if number in nchoosen:
        
        play_game()
        if (board[0:3]==["X","X","X"] or board[3:6]==["X","X","X"] or board[6:9]==["X","X","X"] or board[0:9:4]==["X","X","X"] or board[2:7:2]==["X","X","X"] or board[0:7:3]==["X","X","X"] or board[1:8:3]==["X","X","X"] or board[2:9:3]==["X","X","X"]):   
            print("You Won Cong. :)")
            break
        if nchoosen == []:
            print("Drawww :|")    
            break    
        
        play_game_oppenet()

        if (board[0:3]==["O","O","O"] or board[3:6]==["O","O","O"] or board[6:9]==["O","O","O"] or board[0:9:4]==["O","O","O"] or board[2:7:2]==["O","O","O"] or board[0:7:3]==["O","O","O"] or board[1:8:3]==["O","O","O"] or board[2:9:3]==["O","O","O"]):  
            print("GPU Won  :(")
            break
        if nchoosen == []:
            print("Drawww :|")    
            break    


    else:
        print("Invalid Number Try Again !!!")    