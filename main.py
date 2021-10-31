from robot import Robot
from exceptions import InvalidCommand, InvalidMove, ToyRobotException


COMMAND_PLACE = 'PLACE'
COMMAND_MOVE = 'MOVE'
COMMAND_REPORT = 'REPORT'
COMMAND_LEFT = 'LEFT'
COMMAND_RIGHT = 'RIGHT'
VALID_COMMANDS = frozenset({COMMAND_PLACE, 
                            COMMAND_MOVE, 
                            COMMAND_REPORT, 
                            COMMAND_LEFT, 
                            COMMAND_RIGHT})


class Game:
    def __init__(self):
        self.robot = Robot()
    
    def start(self):
        while True:
            try:
                line = input()
                if line == '':
                    break
                try:
                    self.parse_command(line)
                except ToyRobotException as e:
                    print(e)
                    continue
            except EOFError:
                break

                
    def parse_command(self, line):
        inputs = line.split()
        command = inputs[0]
        if command == COMMAND_PLACE:  
            if len(inputs) != 2:
                raise InvalidCommand('Invalid place command')
            try:
                x, y, facing = inputs[1].split(',')
            except ValueError:
                raise InvalidCommand('invalid location')
            self.robot.place(x, y, facing)
        elif command == COMMAND_MOVE:
            self.robot.move()
        elif command == COMMAND_LEFT:
            self.robot.turn_left()
        elif command == COMMAND_RIGHT:
            self.robot.turn_right()
        elif command == COMMAND_REPORT:
            self.robot.report_location()
        else:
            raise InvalidCommand()


if __name__ == '__main__':
    Game().start()
