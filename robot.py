from exceptions import InvalidMove

MAX_X = 4
MAX_Y = 4
NORTH = 'NORTH'
SOUTH = 'SOUTH'
WEST = 'WEST'
EAST = 'EAST'
DIRECTIONS = frozenset({NORTH, SOUTH, EAST, WEST})


class Robot:
    def __init__(self):
        self.pos_x = None
        self.pos_y = None
        self.facing = None
    
    def in_board(self):
        if self.pos_x is None or self.pos_y is None or self.facing is None:
            return False
        return True

    def place(self, x, y, facing):
        if facing not in DIRECTIONS:
            raise InvalidMove('Invalid Facing Direction')
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            raise InvalidMove('Invalid x or y')
        if x > MAX_X or x < 0 or y > MAX_Y or y < 0:
            raise InvalidMove()
        self.pos_x = x
        self.pos_y = y
        self.facing = facing

    def move(self):
        """
        Move the robot position
        
        if the robot is initialised and within the boundary of the board.

        north -> pos_y += 1
        south -> pos_y -= 1
        east -> pos_x += 1
        west -> pos_x -= 1
        """
        if not self.in_board():
            raise InvalidMove('Not initialised')
        if self.facing == NORTH:
            if self.pos_y == MAX_Y:
                raise InvalidMove()
            self.pos_y += 1
        elif self.facing == SOUTH:
            if self.pos_y == 0:
                raise InvalidMove()
            self.pos_y -= 1
        elif self.facing == EAST:
            if self.pos_x == MAX_X:
                raise InvalidMove()
            self.pos_x += 1
        else:
            if self.pos_x == 0:
                raise InvalidMove()
            self.pos_x -= 1

    def turn_left(self):
        if not self.in_board():
            raise InvalidMove()
        if self.facing == NORTH:
            self.facing = WEST
        elif self.facing == SOUTH:
            self.facing = EAST
        elif self.facing == EAST:
            self.facing = NORTH
        else:
            self.facing = SOUTH


    def turn_right(self):
        if not self.in_board():
            raise InvalidMove()
        if self.facing == NORTH:
            self.facing = EAST
        elif self.facing == SOUTH:
            self.facing = WEST
        elif self.facing == EAST:
            self.facing = SOUTH
        else:
            self.facing = NORTH

    def report_location(self):
        if not self.in_board():
            raise InvalidMove()
        return f'{self.pos_x},{self.pos_y},{self.facing}'
