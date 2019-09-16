from library import multi_move, turn_right, turn_back
def go(turn):
    multi_move(4)
    turn()
    multi_move(4)

move()
turn_left()
multi_move(2)
while object_here():
    take()
turn_back()
multi_move(3)
turn_left()
go(turn_left)
while carries_object():
    put()
turn_back()
go(turn_right)
move()
turn_left()
multi_move(2)
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