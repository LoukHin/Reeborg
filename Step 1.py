from library import multi_move, turn_right, turn_back
multi_move(4)
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