from robot import Robot, InvalidMove
import pytest


@pytest.mark.parametrize("x,y,facing,expected", [
    ('-1', '-1', 'NORTH', InvalidMove), 
    ('0', '-1', 'NORTH', InvalidMove), 
    ('-1', '0', 'NORTH', InvalidMove), 
    ('5', '0', 'EAST', InvalidMove), 
    ('0', '5', 'EAST', InvalidMove), 
    ('0invalid', '5', 'EAST', InvalidMove), 
    ('0', 'invalid', 'EAST', InvalidMove), 
    ('0', '0', 'Invalid', InvalidMove), 
    ('0', '0', 'WEST', None), 
    ('1', '2', 'WEST', None), 
])
def test_robot_place(x, y, facing, expected):
    robot = Robot()
    assert robot.in_board() == False

    if type(expected) == type and issubclass(expected, InvalidMove):
        with pytest.raises(expected):
            robot.place(x, y, facing)
    else:
        robot.place(x, y, facing)
        assert robot.in_board() == True

@pytest.mark.parametrize("x,y,facing,expected", [
    ('0', '0', 'WEST', InvalidMove), 
    ('1', '2', 'WEST', 'Output: 0,2,WEST'), 
    ('4', '2', 'EAST', InvalidMove), 
    ('2', '2', 'EAST', 'Output: 3,2,EAST'), 
    ('2', '0', 'SOUTH', InvalidMove), 
    ('2', '1', 'SOUTH', 'Output: 2,0,SOUTH'), 
    ('2', '4', 'NORTH', InvalidMove), 
    ('2', '1', 'NORTH', 'Output: 2,2,NORTH'), 
])
def test_robot_move(x, y, facing, expected):
    robot = Robot()
    robot.place(x, y, facing)
    if type(expected) == type and issubclass(expected, InvalidMove):
        with pytest.raises(expected):
            robot.move()
    else:
        robot.move()
        assert robot.report_location() == expected

@pytest.mark.parametrize("x,y,facing,expected", [
    ('1', '2', 'WEST', 'Output: 1,2,SOUTH'), 
    ('2', '2', 'EAST', 'Output: 2,2,NORTH'), 
    ('2', '1', 'SOUTH', 'Output: 2,1,EAST'), 
    ('2', '1', 'NORTH', 'Output: 2,1,WEST'), 
])
def test_robot_turn_left(x, y, facing, expected):
    robot = Robot()
    robot.place(x, y, facing)
    robot.turn_left()
    assert robot.report_location() == expected

@pytest.mark.parametrize("x,y,facing,expected", [
    ('1', '2', 'WEST', 'Output: 1,2,NORTH'), 
    ('2', '2', 'EAST', 'Output: 2,2,SOUTH'), 
    ('2', '1', 'SOUTH', 'Output: 2,1,WEST'), 
    ('2', '1', 'NORTH', 'Output: 2,1,EAST'), 
])
def test_robot_turn_right(x, y, facing, expected):
    robot = Robot()
    robot.place(x, y, facing)
    robot.turn_right()
    assert robot.report_location() == expected
