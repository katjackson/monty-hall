import random


def assign_car_door():
    car = random.choice([1, 2, 3])
    return car


def staying_strategy():
    car = assign_car_door()
    first_choice = random.choice([1, 2, 3])
    return first_choice == car


def switching_strategy():
    car = assign_car_door()
    doors = [1, 2, 3]

    first_choice = random.choice(doors)

    return first_choice != car


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
#     car = assign_car_door()
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
