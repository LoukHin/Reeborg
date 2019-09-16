from library import multi_move, turn_right, turn_back
def clear_move():
    while front_is_clear():
        move()
while not is_facing_north():
    turn_left()
turn_back()
clear_move()
turn_left()
clear_move()
turn_back()
count = 1
while 1:
    while object_here():
        take()
    if front_is_clear():
        move()
    else:
        if count%2:
            turn = turn_right
        else:
            turn = turn_left
        turn()
        if front_is_clear():
            move()
            turn()
            count += 1
        else:
            turn_right()
            clear_move()
            break
while carries_object():
    put()
turn_back()
clear_move()
turn_left()
clear_move()
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