from random import choice

guess_count = 0
Max_guess = 5

with open("Hangman.txt", 'r') as f:

    text = f.read().splitlines()  # Reading the file and splitting into seperate words

    while True:                     # Loop to play game multiple times
        print("\n\n\t\tStart game(y/n)?")
        c = input()

        if c == 'y' or c == 'Y':
            while True:
                print("\nHow many guesses do you want?")
                try:
                    Max_guess = int(input())
                    break
                except ValueError:
                    print("\nPlease enter a number.")
            guess_count = 0
            # a list to store already used guesses, to stop repeat letter submittion
            already_used_list = []

            word = choice(text)             # Coosing a random word
            working_word = [' _'] * len(word)

            # joins all the letters in working_word into a single list element and compares with word
            while(guess_count < Max_guess and [''.join(working_word)][0] != word):
                while True:             # Loop to input proper word
                    flag = False
                    print("\n")
                    # Prints the word with any and all correct guess's
                    print(working_word)
                    print("You have " + str(Max_guess - guess_count) +
                          " guesses left.\nEnter your guess:")
                    guess = input()
                    if type(guess) == str and len(guess) == 1:
                        break
                    else:
                        print("\nInvalid input, please enter only 1 character.")

                if guess in already_used_list:
                    guess_count += 1
                    print("\n\tPenelty!\nYou already guessed that one!\nNumber of guess's left = " +
                          str(Max_guess - guess_count))

                else:
                    already_used_list.append(guess)

                    for i in range(len(word)):
                        if (word[i] == guess.lower()):
                            working_word[i] = guess.lower()
                            flag = True
                    if flag:
                        print("\nYou guessed correctly!!")
                    else:
                        guess_count += 1
                        print("\nIncorrect!  Number of guess's left = " +
                              str(Max_guess - guess_count))

            # That is, the full word has been guessed.
            if [''.join(working_word)][0] == word:
                print(
                    "\n\n\t\tCongradulations!\n\t\tYou win!\nThe word was: " + word + "\n\n\n\nYou may play again or exit now...")
            else:
                print("\n\n\t\tYou ran out of guesses.Too bad.\n\nThe word was: " +
                      word + "\n\n\nYou may play again or exit now...")

        elif c == 'n' or c == 'N':
            print("\n\nExiting game...")
            break

        else:
            print("\n\nPlease enter y/Y to start the game and n/N to exit.")

    print('Thanks for playing Hangman!')
