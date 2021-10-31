from main import Game
from exceptions import InvalidMove, InvalidCommand, ToyRobotException

import pytest

@pytest.fixture
def mock_robot(mocker):
    mock = mocker.patch('main.Robot')
    return mock

@pytest.mark.parametrize("command,expected", [
    ('PLACE 0,WEST', InvalidCommand), 
    ('PLACE', InvalidCommand), 
    ('PLACE 0,0,WEST invalid', InvalidCommand), 
    ('Move', InvalidCommand), 
    ('otherCommand', InvalidCommand), 
    ('PLACE 0,0,WEST', None), 
])
def test_game_invalid_command(command, expected, mocker, mock_robot):
    game = Game()
    robot_obj = mock_robot.return_value
    if type(expected) == type and issubclass(expected, ToyRobotException):
        with pytest.raises(expected):
            game.parse_command(command)
    else:
        game.parse_command(command)
        assert robot_obj.place.called


@pytest.mark.parametrize("init_command, command,expected", [
    ('PLACE 0,0,WEST', "REPORT", "Output: 0,0,WEST"), 
    ('PLACE 0,0,WEST', "MOVE", InvalidMove), 
    ('PLACE 4,0,EAST', "MOVE", InvalidMove),
    ('PLACE 4,0,EAST', "MOVE", InvalidMove), 
    ('PLACE 2,2,EAST', "RIGHT", "Output: 2,2,SOUTH"),
    ('PLACE 2,2,EAST', "LEFT", "Output: 2,2,NORTH"),
])
def test_game_command(init_command, command, expected):
    game = Game()
    game.parse_command(init_command)
    if type(expected) == type and issubclass(expected, ToyRobotException):
        with pytest.raises(expected):
            game.parse_command(command)
    else:
        game.parse_command(command)
        assert game.robot.report_location() == expected
