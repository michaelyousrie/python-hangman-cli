import words as game_words
import hangman_art as hangman
import os

def main():
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')
    #enddef

    def display_divider(times=20, symbol="*"):
        print(symbol * times)
    #enddef

    def display_hint(hint):
        print(" ".join(hint))
    #enddef

    def display_man(stage):
        display_divider()
        for line in hangman.draw_hangman(stage):
            print(line)
        #endfor
        display_divider()
    #enddef

    def new_line():
        print()
    #enddef

    def start_game():
        secret_word = game_words.get_random_word()
        max_guesses = remaining_guesses = 6
        hint = ["_"] * len(secret_word)

        while remaining_guesses >= 0:
            clear_terminal()

            if remaining_guesses == 0:
                display_man(max_guesses)
                print("The man was hanged!")
                display_divider(times=50)
                print(f"The correct word was: {secret_word}")
                display_divider(times=50)
                break
            #endif

            display_man(max_guesses - remaining_guesses)
            display_hint(hint)
            new_line()

            guess = input('Enter a single letter: ').lower()

            if len(guess) > 1 or not guess.isalpha():
                print('Enter only a single letter please')
                continue
            #endif

            if not guess in secret_word:
                display_divider(symbol='=')
                print(f"{guess} is not in the word")
                display_divider(symbol='=')
                remaining_guesses -= 1
                print(f"Remaining Guesses: {remaining_guesses}")
                continue
            #endif

            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    hint[i] = guess
                #endif
            #endfor

            if "_" not in hint:
                clear_terminal()
                print("You've won the game!!")
                break
            #endif
        #endwhile
    #enddef
    while True:
        try:
            play_again = input("Would you like to start the game? (Y/N): ").upper()
        except KeyboardInterrupt:
            print("Have a nice day!")
            exit()
        #endtry

        if (play_again == 'Y' or play_again == 'YES'):
            start_game()
        else:
            break
        #endif
    #endwhile
    print("Have a nice day!")
#enddef


if __name__ == "__main__":
    main()
#endif