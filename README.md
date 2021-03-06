# toy_robot

## Running Environment
This program is tested with Python3.7 and Python3.8 on Linux and Mac OS.

## Game instructions
This program simulates a robot movement on a 5x5 unit board, and accepts the following commands:
```
PLACE <x>.<y>.<direction>
MOVE
LEFT
RIGHT
REPORT
```

## How to run this program
This program can be run via command line
```
python main.py

PLACE 0,0,NORTH
MOVE
...<OTHER COMMAND>
<empty command to exit the program>
```

And type in the correct commands listed above

alternatively, this program can accept input from text file with commands
```
cat testfile1 | python main.py
```

## Running the test
This program uses tox to automate the tests process.
Please install `tox` using `pip install tox` , and run the test via following command
```
tox
```

Test report:

```
collected 39 items

tests/test_main.py .............                                                                                                             [ 33%]
tests/test_robot.py ..........................                                                                                               [100%]

---------- coverage: platform darwin, python 3.7.5-final-0 -----------
Name                  Stmts   Miss  Cover
-----------------------------------------
exceptions.py             6      0   100%
main.py                  43      4    91%
robot.py                 72      4    94%
tests/__init__.py         0      0   100%
tests/test_main.py       30      0   100%
tests/test_robot.py      29      0   100%
-----------------------------------------
TOTAL                   180      8    96%


================================================================ 39 passed in 0.24s ================================================================
_____________________________________________________________________ summary ______________________________________________________________________
  python: commands succeeded
  congratulations :)
```
