'''this is the code that works'''
secret_word = 'tiffany'
user_guess = ''
turns = 12
while turns > 0:
    failed = False
    for letter in secret_word:
        if letter not in user_guess:
            print("_")
            failed += 1
        else:
            print(letter)
    if failed == True:
        print("You won!")
    guess = input("please guess a letter:")
    user_guess += guess
    if guess not in secret_word:
        print('incorrect!')
        turns -=1
        if turns == 0:
            failed == 1
            print("you lose!")