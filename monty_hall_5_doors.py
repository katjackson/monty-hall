import random


def assign_car_door():
    doors = [1, 2, 3, 4, 5]
    car = random.choice(doors)
    return car


def staying_strategy():
    car = assign_car_door()
    first_choice = random.choice([1, 2, 3, 4, 5])
    return first_choice == car


def open_a_door(doors, car):
    doors.remove(car)
    open_door = random.choice(doors)
    doors.remove(open_door)
    doors.append(car)
    return doors


def switching_strategy():
    car = assign_car_door()
    doors = [1, 2, 3, 4, 5]

    first_choice = random.choice(doors)
    doors.remove(first_choice)

    if first_choice != car:
        doors = open_a_door(doors, car)

    second_choice = random.choice(doors)
    return second_choice == car


staying_wins = 0
switching_wins = 0

for _ in range(10000):
    if staying_strategy():
        staying_wins += 1

for _ in range(10000):
    if switching_strategy():
        switching_wins += 1

print('Probability of staying win: {}%'.format(staying_wins / 100))
print('Probability of switching win: {}%'.format(switching_wins / 100))
