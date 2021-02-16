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