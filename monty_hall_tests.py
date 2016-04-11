from unittest.mock import patch
import monty_hall


def test_assign_car_door():
    with patch('random.choice', return_value=3):
        choice = monty_hall.assign_car_door()
        assert (choice == 3)


def test_staying_strategy():
    with patch('monty_hall.assign_car_door', return_value=3):
        with patch('random.choice', return_value=3):
            win = monty_hall.staying_strategy()
            assert (win)
        with patch('random.choice', return_value=2):
            win = monty_hall.staying_strategy()
            assert (not win)


def test_switching_strategy():
    with patch('monty_hall.assign_car_door', return_value=3):
        with patch('random.choice', return_value=3):
            win = monty_hall.switching_strategy()
            assert (not win)
        with patch('random.choice', return_value=2):
            win = monty_hall.switching_strategy()
            assert (win)
