from random import randint

colors = ['Red', 'Yellow', 'Orange', 'Green', 'Blue']
user_choice = 0
computer_choice = 0
user_points = 0
computer_points = 0

def start_game():
    global user_choice
    print('Great, lets start.')
    print('Look at the options:')
    for index, value in enumerate(colors):
        print(index + 1, value)
    user_choice = int(input('Choose one color from {} to {}! '.format(1, len(colors))))
    if user_choice < 1 or user_choice > len(colors):
        print('Your choice is not valid. Try again.')
        start_game()
    user_choice -= 1
    print('Your choice is {}'.format(colors[user_choice]))
    check_who_win()

def end_game():
    play_again = input('Do you want play again? (y or n)')
    if play_again.lower() == 'y':
        start_game()
    elif play_again.lower() == 'n':
        print('It was a pleasure to play with you. Thanks')
    else:
        print('This answer is not valid. Please, try again.')
        end_game()

def check_who_win():
    global computer_choose
    global computer_points
    global user_points
    computer_choice = randint(0, len(colors) - 1)
    #print(computer_choice)
    print('My choice is {}'.format(colors[computer_choice]))
    if computer_choice == user_choice:
        print('You win!')
        user_points += 1
    else:
        print('I win!')
        computer_points += 1
    show_scores()
    
        

def show_scores():
    print('The actual score is:')
    print('You: ', user_points)
    print('Me: ', computer_points)
    if user_points > computer_points:
        print('You are winning')
    elif user_points < computer_points:
        print('I am winning')
    else:
        print('The game is tied')
    end_game()


start_game()