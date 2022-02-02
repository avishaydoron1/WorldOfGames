from WorlsOfGames.games import MemoryGame, CurrencyRoulette, GuessGame

1




chosen_game = 0
chosen_difficult_game = 0

def welcome(name):
    print(f'''Hello {name} and welcome to the World of Games (WoG).
Here you can find many cool games to play.
''')

#welcome("avishay")


def load_game():
    chosen_game = int(input('''Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to
guess it back
2. Guess Game - guess a number and see if you chose like the computer
3. Currency Roulette - try and guess the value of a random amount of USD in ILS'''))
    if chosen_game <= 3  and chosen_game >= 1 :
        pass
    else:
        print("your chosen not exist , please try again")
        load_game()


    chosen_difficult_game = int(input("Please choose game difficulty from 1 to 5:"))
    if chosen_difficult_game <= 5  and chosen_difficult_game >= 1 :
       pass
    else:
        print("your chosen not exist , please try again")
        load_game()
    if chosen_game == 1:
        MemoryGame.play_memory_game(chosen_difficult_game)
    elif chosen_game == 2:
        GuessGame.play_guess_game(chosen_difficult_game)
    elif chosen_game == 3:
        CurrencyRoulette.play_currency_roulette(chosen_difficult_game)






#load_game()



