## Simulating the Monty Hall Problem

### Monty Hall
The monty_hall.py file simulates two versions of the Monty Hall game and returns the winning percentages for both. The *staying strategy* simulates a game in which the player sticks with their original guess throughout the game. The *switching_strategy* simulates a game in which the player switches their guess after a non-winning door is ruled out. Each simulation is run 1000 times, producing win percentages of around 33.3% for the *staying strategy* and 66.7% for the *switching strategy*. Separate file includes mock tests.

#### Monty Hall (5 Doors)
The monty_hall_5_doors.py file simulates the same two game strategies, but for a game with 5 door choices. Each strategy simulation is run 10000 times. The *staying strategy* produces a winning percentage of around 20%, while the *switching_strategy* provides about a 26.7% chance of winning. Separate file includes mock tests.

### Analysis
The result of the four simulations leads to the following assumptions. The chance of winning with your first choice is 1/n for the number of choices. The chance of winning if you switch choices after one is ruled out is ( (n-1/n) / n-2 ), which is always slightly higher than the probability of winning using the staying strategy.
