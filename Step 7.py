from library import multi_move, turn_right, turn_back
def mov_n_put(count=1):
    for _ in range(count):
        move()
        put()

def draw(num):
    if num:
        move()
        turn_left()
        mov_n_put(5)
        turn_back()
        multi_move(5)
        turn_left()
        move()
    else:
        move()
        turn_left()
        mov_n_put(5)
        turn_right()
        mov_n_put(2)
        turn_right()
        mov_n_put(4)
        turn_right()
        mov_n_put()
        for _ in range(2):
            turn_left()
            move()
        move()

draw(1)
draw(0)
draw(0)
draw(1)
draw(0)
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