from currency_converter import CurrencyConverter
import random
import Score


def play_currency_roulette(num):
    Difficulty = num
    amount = random.randint(1,100)
    user_input = int(input("How much is" +" " + str(amount)+" " + "in Shekels ? "))
    converter = CurrencyConverter()
    real_value =converter.convert(amount, 'USD', 'ILS')
    print(real_value)  

    #limits of value by Difficulty
    upper_limit = real_value + (5-Difficulty)
    lower_limit = real_value - (5-Difficulty)

    #check user guess
    if user_input > lower_limit and user_input < upper_limit:
        print("Greate guess , your score is")
        Score.add_score(Difficulty)
        print("your total score is")
        Score.calc_total_score()
    else:
        print("Wrong Guess")