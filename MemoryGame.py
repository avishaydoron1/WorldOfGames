import random
import time
import Score
import Utils


def play_memory_game(num):
    Difficulty = num


    random_list = random.sample(range(1, 101), Difficulty)
    print(random_list)
    time.sleep(0.8)
    Utils.clear_screen()
    user_input = input("Please enter numbers with white space between")
    user_list = user_input.split()
    map_object = map(int, user_list)
    list_user = list(map_object)
    print(list_user)

    if (list_user == random_list):
        print("YOU HAVE GOOD MEMORY , your score is")
        Score.add_score(Difficulty)
        print("your total score is")
        Score.calc_total_score()
    else:
        print("Wrong answer")
