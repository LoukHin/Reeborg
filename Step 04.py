from library import multi_move, turn_right, turn_back
multi_move(3)
turn_left()
multi_move(2)
take()
turn_right()
multi_move(4)
put()
turn_right()
multi_move(2)
take()
turn_right()
multi_move(2)
turn_left()
multi_move(3)
put()
move()
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