import os

scores_file_name = 'scores_file_name.txt'
BAD_RETURN_CODE = 400

#Screen_cleaner - A function to clear the screen
def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


