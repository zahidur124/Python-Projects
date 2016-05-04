##
## ***************************************************
## Zahidur Abedin (20549852)
## CS 116 Winter 2015
## Assignment 05, Problem 4
## ***************************************************
##


## Helper function for fib_rec
## fib_acc(n,n0,last,prev) produces the nth Fibonacci number
##    using the n0th Fibonacci number (last) and the (n0-1)th Fibonacci number (prev)
## fib_acc: Nat Nat Nat Nat -> Nat
## requires: n0 <= n
def fib_acc(n,n0,last,prev):
    if n==n0:
        return last
    else:
        return fib_acc(n,n0+1,last+prev,last)
    
## fib_rec(n) produces the nth Fibonacci number
## fib_rec: Nat -> Nat
## Examples: 
## * fib_rec(0) => 0
## * fib_rec(10) => 55
def fib_rec(n):
    if n==0:
        return 0
    else:
        return fib_acc(n,1,1,0)

#computer_decision(n) consumes n, a natural number, and produces calculates
# the remainder of the fibonacci number of n when divided by 3 and produces
# a string depending on the remainder. If the remainder is 0, 'r' is produced,
# 'p' if remainder is 1, and 's' otherwise.
#computer_decision: Nat -> Str

def computer_decision(n):
    remainder = fib_rec(n)%3
    if remainder == 0:
        return "r"
    elif remainder == 1:
        return "p"
    else:
        return "s"
    
#play_rps() consumes None and produces a Rock-Paper-Scissor game that 
# interacts with the user. The game continues as long as the user does not
# enter 'q'. Upon entering 'q', the game quits and produces the overall
# score-track of the game between the user and the computer
#play_rps(): None -> None
# requires: input to be one of "q","r","s","p"
#Examples:
#         play_rps() produces the Rock-Paper-Scissor game. Entering the list
#         of strings ["r","s","p","s","q"], prints the output of the total
#         game statistics, where there are 0 tied games,player won 1 games,
#         and computer won 2 games.

welcome_message = "Welcome to the Rock-Paper-Scissors game!"
prompt = "How would you like to play next [r/p/s/q]?"
goodbye_message = "Thank you for playing! Total game statistics:"

def play_rps():
    tied_games = 0
    player_won = 0
    computer_won = 0
    game_count = 1
    print(welcome_message)
    print(prompt)
    player_input = input()
    while not (player_input == 'q'):
        if player_input == computer_decision(game_count):
            tied_games = tied_games + 1
            print("Player plays: {0}. Computer plays: {1}. Game tied." \
                  .format(player_input,computer_decision(game_count)))            
            game_count = game_count + 1
            print(prompt)
            player_input = input()
        elif player_input == 'r' and computer_decision(game_count) == 's':
            player_won = player_won + 1
            print("Player plays: {0}. Computer plays: {1}. Player won." \
                  .format(player_input,computer_decision(game_count)))            
            game_count = game_count + 1
            print(prompt)
            player_input = input()
        elif player_input == 'p' and computer_decision(game_count) == 'r':
            player_won = player_won + 1
            print("Player plays: {0}. Computer plays: {1}. Player won." \
                  .format(player_input,computer_decision(game_count)))            
            game_count = game_count + 1
            print(prompt)
            player_input = input()
        elif player_input == 's' and computer_decision(game_count) == 'p':
            player_won = player_won + 1
            print("Player plays: {0}. Computer plays: {1}. Player won." \
                  .format(player_input,computer_decision(game_count)))            
            game_count = game_count + 1
            print(prompt)
            player_input = input()
        elif player_input == 'p' and computer_decision(game_count) == 's':
            computer_won = computer_won + 1
            print("Player plays: {0}. Computer plays: {1}. Computer won." \
                  .format(player_input,computer_decision(game_count)))              
            game_count = game_count + 1 
            print(prompt)
            player_input = input()
        elif player_input == 'r' and computer_decision(game_count) == 'p':
            computer_won = computer_won + 1
            print("Player plays: {0}. Computer plays: {1}. Computer won." \
                  .format(player_input,computer_decision(game_count)))              
            game_count = game_count + 1 
            print(prompt)
            player_input = input()
        else: 
            computer_won = computer_won + 1
            print("Player plays: {0}. Computer plays: {1}. Computer won." \
                  .format(player_input,computer_decision(game_count)))              
            game_count = game_count + 1 
            print(prompt)
            player_input = input()
    print(goodbye_message)
    print("Tied games: {}.".format(tied_games))
    print("Player won" , player_won , "times.")
    print("Computer won" , computer_won, "times.")
    
#Tests:


    