from library import multi_move, turn_right, turn_back
def go(direction):
    if direction == "l":
        first_turn = turn_right
        turn = turn_left
    else:
        first_turn = turn_left
        turn = turn_right
    first_turn()
    multi_move(2)
    turn()
    multi_move(3)
    turn()
    multi_move(2)
    turn()
go("l")
take()
go("r")
put()
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