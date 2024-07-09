# https://www.codewars.com/kata/5bb904724c47249b10000131/train/python

def points(games):

    points = 0

    for i in games:
        team = i[0:1]
        opponent = i[2:3]

        if team > opponent:
            points += 3
        elif team < opponent:
            points += 0
        elif team == opponent:
            points += 1

    return points
