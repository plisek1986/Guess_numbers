def user_choice():
    """
    This functions is focused on the user and his feedback to computer's number

    Returns: Answer from the user (str)

    """
    # defining available answers from the user
    available_answers = ['too small', 'too big', 'you win']
    # while loop and condition to check if the answer from the user meets the evaluation criteria
    while True:
        user_answer = input().lower()
        if user_answer in available_answers:
            break
        print('Incorrect value provided')
    return user_answer


def guessing_number():
    """
    This code simulates the game of making guesses by the computer

    Returns: Guess value for the choice from computer (str)

    """
    print('Imagine a number between 0 and 1000 and hit ENTER')
    # adds line so that you can hit ENTER without unsolicited consequences
    input()
    # defining min and max values
    min_nb = 0
    max_nb = 1000
    # this line is added so that reference before assignment error is not shown
    user_answer = ''
    # while loop to continue until the user provides answer 'you win'
    while user_answer != 'you win':
        guess = (max_nb - min_nb) / 2 + min_nb
        print(f'Your number is {guess}')
        # lodging user_choice function in the guessing_number function
        user_answer = user_choice()
        if user_answer == 'too small':
            min_nb = guess
        elif user_answer == 'too big':
            max_nb = guess
        else:
            return 'Great, you have just won!'

guessing_number()