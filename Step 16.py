from library import multi_move, turn_right, turn_back
def turn():
    if is_facing_north():
        turnx = turn_right
    else:
        turnx = turn_left
    turnx()
    move()
    turnx()

multi_move(2)
turn_left()
move()
for _ in range(6):
    move()
    for _ in range(6):
        if object_here():
            take()
        move()
    turn()
turn_back()
move()
while carries_object():
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