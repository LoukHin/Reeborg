from library import multi_move, turn_right, turn_back
def go_take(direction):
    if direction == "l":
        turn = turn_left
    else:
        turn = turn_right
    move()
    turn()
    for _ in range(2):
        move()
        take()
    turn_back()
    multi_move(2)
    while carries_object():
        put()
    turn()
go_take("l")
go_take("r")
go_take("l")
go_take("r")
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