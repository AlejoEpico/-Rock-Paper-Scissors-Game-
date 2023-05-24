import random

exit = False
user_points = 0
computer_points = 0

while not exit:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors, or exit: ").lower()
    computer_input = random.choice(options)
    
    if user_input == 'exit':
        print('Game ended')
        exit = True
        
    elif user_input in options:
        if user_input == 'rock':
            if computer_input == 'rock':
                print('Your input is rock')
                print('Computer input: rock')
                print('It is a tie!')
                
            elif computer_input == 'paper':
                print('Your input is rock')
                print('Computer input: paper')
                print('Computer wins!')
                computer_points += 1 
                
            elif computer_input == 'scissors':
                print('Your input is rock')
                print('Computer input: scissors')
                print('You win!')
                user_points += 1 
                
        elif user_input == 'paper':
            if computer_input == 'rock':
                print('Your input is paper')
                print('Computer input: rock')
                print('You win!')
                user_points += 1
                
            elif computer_input == 'paper':
                print('Your input is paper')
                print('Computer input: paper')
                print('It\'s a tie!')
                
            elif computer_input == 'scissors':
                print('Your input is paper')
                print('Computer input: scissors')
                print('Computer wins!')
                computer_points += 1 
                
        elif user_input == 'scissors':
            if computer_input == 'rock':
                print('Your input is scissors')
                print('Computer input: rock')
                print('Computer wins!')
                computer_points += 1 
                
            elif computer_input == 'paper':
                print('Your input is scissors')
                print('Computer input: paper')
                print('You win!')
                user_points += 1
                
            elif computer_input == 'scissors':
                print('Your input is scissors')
                print('Computer input: scissors')
                print('It\'s a tie!')
            
    else:
        print('Invalid input')
