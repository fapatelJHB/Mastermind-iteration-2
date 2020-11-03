import random


# TODO: Decompose into functions


    #print(code)
def print_beginning():
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')

    global code 
    code = [0,0,0,0]
    for i in range(0, 4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value

def main_game(code):    
    '''
    Code for the game. Inputs and digits
    '''
    correct = False
    turns = 0 
    while not correct and turns < 12:
        answer = input("Input 4 digit code: ")
        if len(answer) < 4 or len(answer) > 4:
            print("Please enter exactly 4 digits.")
            continue
        correct_digits_and_position = 0
        correct_digits_only = 0
        for i in range(len(answer)):
            if code[i] == int(answer[i]):
                correct_digits_and_position += 1
            elif int(answer[i]) in code:
                correct_digits_only += 1

        print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
        print('Number of correct digits not in correct place: '+str(correct_digits_only))
        turns += 1

        if correct_digits_and_position == 4:
            correct = True
            print('Congratulations! You are a codebreaker!')
            print('The code was: '+str(code))
        else:
            print('Turns left: '+str(12 - turns))

def run_game():
    print_beginning()
    main_game(code)

if __name__ == "__main__":
    run_game()
