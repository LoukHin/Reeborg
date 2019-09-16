from library import multi_move, turn_right, turn_back
move()
turn_right()
move()
while not at_goal():
    if right_is_clear():
        turn_right()
        build_wall()
        turn_left()
    elif not front_is_clear():
        turn_left()
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