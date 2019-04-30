# In the game of darts a player throws three darts at
# a target board which is split into twenty equal sized
# sections numbered one to twenty.
# The score of a dart is determined by the number of the
# region that the dart lands in. A dart landing outside
# the red/green outer ring scores zero. The black and
# cream regions inside this ring represent single scores.
# However, the red/green outer ring and middle ring score
# double and treble scores respectively.
# At the centre of the board are two concentric circles
# called the bull region, or bulls-eye. The outer bull
# is worth 25 points and the inner bull is a double,
# worth 50 points.
# There are many variations of rules but in the most
# popular game the players will begin with a score 301
# or 501 and the first player to reduce their running
# total to zero is a winner. However, it is normal to
# play a "doubles out" system, which means that the player
# must land a double (including the double bulls-eye at
# the centre of the board) on their final dart to win;
# any other dart that would reduce their running total
# to one or lower means the score for that set of three
# darts is "bust".
# When a player is able to finish on their current score
# it is called a "checkout" and the highest checkout is
# 170: T20 T20 D25 (two treble 20s and double bull).
# Note that D1 D2 is considered different to D2 D1 as
# they finish on different doubles. However, the combination
# S1 T1 D1 is considered the same as T1 S1 D1.
# In addition we shall not include misses in considering
# combinations; for example, D3 is the same as 0 D3 and 0 0 D3.
# How many distinct ways can a player checkout with a
# score less than 100?
# ----------------------------------------------------
# Analysis: brute force

MAX_SCORE = 100
MULTIPLE = {'S': 1, 'D': 2, 'T': 3}
possible_dart = [m + str(s) for m in 'SDT' for s in range(1, 21)] + ['S25', 'D25']
score = dict(zip(possible_dart, map(lambda s: MULTIPLE[s[0]] * int(s[1:]), possible_dart)))
possible_checkout = set()
for final_dart in possible_dart:
    if final_dart[0] == 'D':
        s = score[final_dart]
        if s < MAX_SCORE:
            possible_checkout.add((final_dart, ))
            for second_dart in possible_dart:
                s += score[second_dart]
                if s < MAX_SCORE:
                    possible_checkout.add((final_dart, second_dart))
                    for first_dart in possible_dart:
                        s += score[first_dart]
                        if s < MAX_SCORE:
                            possible_checkout.add(tuple([final_dart] + sorted([second_dart, first_dart])))
                        s -= score[first_dart]
                s -= score[second_dart]

print(len(possible_checkout))