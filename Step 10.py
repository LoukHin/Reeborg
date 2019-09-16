from library import multi_move, turn_right, turn_back
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
for _ in range(6):
    jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def multi_move(count=1):
    for _ in range(count):
        move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
   
def turn_back():
    turn_left()
    turn_left()