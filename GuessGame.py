import random
import Score

def play_guess_game(num):

    Difficulty = num
    Secret_number = int(input("Welcom to guess game please enter number"))

    game_random_number = random.randint(1,Difficulty)
    print(game_random_number)

    if Secret_number == game_random_number:
        print("Good guess , your score is")
        Score.add_score(Difficulty)
        print("your total score is")
        Score.calc_total_score()

    else:
        print("wrong guess try again")

