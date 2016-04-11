import random


def assign_doors():
    doors = [1, 2, 3]
    game = {'a_goat': 0, 'b_goat': 0, 'car': 0}

    game['a_goat'] = random.choice(doors)
    doors.remove(game['a_goat'])

    game['b_goat'] = random.choice(doors)
    doors.remove(game['b_goat'])

    game['car'] = doors[0]

    return game


def staying_strategy():
    game = assign_doors()
    first_choice = random.choice([1, 2, 3])
    return first_choice == game['car']


def switching_strategy():
    game = assign_doors()
    doors = [1, 2, 3]

    first_choice = random.choice(doors)
    doors.remove(first_choice)

    if first_choice == game['a_goat']:
        doors.remove(game['b_goat'])

    elif first_choice == game['b_goat']:
        doors.remove(game['a_goat'])

    second_choice = doors[0]
    return second_choice == game['car']


staying_wins = 0
switching_wins = 0

for _ in range(1000):
    if staying_strategy():
        staying_wins += 1

for _ in range(1000):
    if switching_strategy():
        switching_wins += 1

print('Probability of staying win: {}%'.format(staying_wins / 10))
print('Probability of switching win: {}%'.format(switching_wins / 10))


# def game_loop():
#     game = assign_doors()
#     first_choice = random.choice([1, 2, 3])
#     if first_choice == game['car']:
#         return 'staying win'
#     else:
#         return 'switching win'
#
# staying_wins = 0
# switching_wins = 0
#
# for _ in range(1000):
#     win = game_loop()
#     if win == 'staying win':
#         staying_wins += 1
#     elif win == 'switching win':
#         switching_wins += 1
#
# probability_of_switching_wins = switching_wins / 1000
# print(probability_of_switching_wins)
