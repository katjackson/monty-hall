from unittest.mock import patch
import monty_hall_5_doors


def test_assign_car_door():
    with patch('random.choice', return_value=2):
        car = monty_hall_5_doors.assign_car_door()
        assert (car == 2)


def test_staying_strategy():
    with patch('monty_hall_5_doors.assign_car_door', return_value=2):
        with patch('random.choice', return_value=2):
            win = monty_hall_5_doors.staying_strategy()
            assert (win)
        with patch('random.choice', return_value=1):
            win = monty_hall_5_doors.staying_strategy()
            assert (not win)


def test_switching_strategy():
        with patch('monty_hall_5_doors.assign_car_door', return_value=1):
            with patch('random.choice', return_value=2):
                with patch('monty_hall_5_doors.open_a_door',
                           return_value=[1, 4, 5]
                           ):
                    with patch('random.choice', return_value=1):
                        win = monty_hall_5_doors.switching_strategy()
                        assert (win)
                    with patch('random.choice', return_value=4):
                        win = monty_hall_5_doors.switching_strategy()
                        assert (not win)
            with patch('random.choice', return_value=1):
                win = monty_hall_5_doors.switching_strategy()
                assert (win)
