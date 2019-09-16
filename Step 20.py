from library import multi_move, turn_right, turn_back
multi_move(3)
turn_right()
move()
while not at_goal():
    if right_is_clear():
        move()
        if wall_on_right():
            turn_back()
            move()
            turn_left()
            build_wall()
            turn_left()
        else:
            turn_back()
            move()
            turn_left()
            move()
    elif front_is_clear():
        move()
    else:
        turn_left()
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