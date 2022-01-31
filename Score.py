

def add_score(Difficulty):
    points_of_winning = (Difficulty*3)+5
    print(points_of_winning)
    points = open("scores_file_name", "a")
    points.write(str(points_of_winning) + '\n')
    points.close()

def calc_total_score():
    score = 0
    Total_points = open("scores_file_name", "r")
    for i in Total_points:
        score =  int(score) + int(i)
    print(score)
    Total_points.close()





