from library import multi_move, turn_right, turn_back
move()
def tak_n_mov():
    take()
    move()

for _ in range(3):
    tak_n_mov()

while carries_object():
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